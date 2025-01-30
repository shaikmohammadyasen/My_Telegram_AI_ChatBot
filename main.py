import pytesseract  # Add this if not already imported
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InputFile, PhotoSize, Document
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from textblob import TextBlob  # Sentiment Analysis
from config import TOKEN
from mongo_db import store_user_data, store_chat_in_mongo, is_user_registered, save_user_phone, store_file_metadata
from gemini_api import query_gemini  # Gemini AI integration
from file_processing import process_image, process_pdf  # File processing utilities
import requests

# Ensure pytesseract uses the correct path to tesseract.
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Web search function using SerpAPI
def web_search(query: str):
    API_KEY = "ddf21c9d1bec1a2fd50c0798de2e7cd1d73f8fab73b9a9ea7a83e16d52239a72"  # Replace with your API Key
    url = f"https://serpapi.com/search?q={query}&api_key={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        search_results = []
        for result in data.get('organic_results', []):
            title = result.get('title')
            link = result.get('link')
            snippet = result.get('snippet')
            search_results.append(f"**{title}**\n{snippet}\n[Link]({link})\n")
        return "\n".join(search_results) if search_results else "No relevant results found."
    else:
        return "An error occurred while fetching the search results."

# Web search command handler
async def web_search_command(update: Update, context: CallbackContext) -> None:
    user_input = " ".join(context.args)  # Get the search query from the user's message
    
    if user_input:
        results = web_search(user_input)  # Call the web search function
        await update.message.reply_text(results)  # Send the results back to the user
    else:
        await update.message.reply_text("Please provide a search query after the /websearch command.")

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    chat_id = update.message.chat_id

    # Check if user is registered in MongoDB
    if not is_user_registered(chat_id):
        store_user_data(chat_id, user.first_name, user.username)
        phone_button = KeyboardButton("Share Contact", request_contact=True)
        reply_markup = ReplyKeyboardMarkup([[phone_button]], one_time_keyboard=True)
        await update.message.reply_text("Hello! Please share your phone number for registration.", reply_markup=reply_markup)
    else:
        welcome_text = "Welcome back! Send an image, PDF, or type something for assistance."
        await update.message.reply_text(welcome_text)

# Help command to guide users
async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Welcome! Here’s what you can do:\n"
        "/start - Register & start\n"
        "/help - Get help\n"
        "/websearch - Web search\n"
        "Send me an image/PDF to analyze!"
    )
    await update.message.reply_text(help_text)

# Handle contact information
async def handle_contact(update: Update, context: CallbackContext) -> None:
    phone_number = update.message.contact.phone_number
    chat_id = update.message.chat_id

    save_user_phone(chat_id, phone_number)
    await update.message.reply_text("Thanks for sharing your phone number! You're registered.")

# Sentiment Analysis & Gemini AI Chat
async def gemini_chat(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    chat_id = update.message.chat_id

    # Sentiment Analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    
    if sentiment > 0:
        sentiment_feedback = "😊 That sounds great! Keep up the positivity!"
    elif sentiment < 0:
        sentiment_feedback = "😔 I sense some negativity. I'm here if you need support!"
    else:
        sentiment_feedback = "😐 I understand. Let me know how I can help."

    # Query Gemini AI
    response = query_gemini(user_input)
    
    # Store chat & sentiment in MongoDB
    store_chat_in_mongo(user_input, response, chat_id)
    
    # Send response with sentiment feedback
    await update.message.reply_text(f"{sentiment_feedback}\n\n{response}")

# Handle file uploads (image, PDF)
async def handle_file(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    try:
        file = update.message.document or update.message.photo[-1]  # Get file

        if isinstance(file, Document) and file.mime_type == 'application/pdf':
            file_id = file.file_id
            file = await context.bot.get_file(file_id)
            await file.download_to_drive('user_file.pdf')

            text = process_pdf('user_file.pdf')
            analysis = query_gemini(text)

            store_file_metadata(file.file_id, 'PDF', text, analysis, chat_id)

            await update.message.reply_text(f"📄 Extracted & analyzed PDF:\n{analysis}")

        elif isinstance(file, PhotoSize):
            file_id = file.file_id
            file = await context.bot.get_file(file_id)
            await file.download_to_drive('user_image.jpg')

            # Process image with OpenCV before OCR
            text = process_image('user_image.jpg')
            analysis = query_gemini(text)

            store_file_metadata(file.file_id, 'Image', text, analysis, chat_id)

            await update.message.reply_text(f"🖼️ Extracted & analyzed image:\n{analysis}")

        else:
            await update.message.reply_text("❌ Unsupported file type. Please send a PDF or an image.")
    
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error processing your file: {str(e)}")

# Create the bot application
app = Application.builder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("websearch", web_search_command))
app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gemini_chat))  # Sentiment-aware chat
app.add_handler(MessageHandler(filters.PHOTO, handle_file))
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

# Start polling
if __name__ == "__main__":
    print("🤖 Bot is running with Sentiment Analysis, AI chat, and File Processing!")
    app.run_polling()
