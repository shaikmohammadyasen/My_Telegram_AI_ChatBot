from telegram import Update
from telegram.ext import ContextTypes
from mongo_db import store_chat_in_mongo
from gemini_api import query_gemini

async def gemini_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = query_gemini(user_input)
    store_chat_in_mongo.insert_one({
        "chat_id": update.message.chat_id,
        "user_input": user_input,
        "bot_response": response,
        "timestamp": update.message.date,
    })
    await update.message.reply_text(response)