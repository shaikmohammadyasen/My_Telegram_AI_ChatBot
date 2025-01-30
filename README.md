# My_Telegram_AI_ChatBot

## Project Description

The **Telegram AI ChatBot** is an intelligent bot designed to interact with users via the Telegram platform. It integrates various technologies to offer multiple functionalities, including image and file processing, sentiment analysis and  web search capabilities. This bot provides responses and performs analysis based on the user's queries and shared files. 
The bot is powered by the **Gemini API** for handling natural language queries, and **MongoDB Atlas** is used to store user data for better interaction and functionality.

## Features
- **Image Analysis**: The bot is capable of processing images and extracting text from them using OCR (Optical Character Recognition) techniques.
- **File Processing**: The bot can analyze PDF files and extract text for users.
- **Sentiment Analysis**: Implements sentiment analysis to detect whether a user's message conveys a positive, negative, or neutral tone.
- **Web Search**: Integrates with **SerpAPI** to fetch search results from the web.
- **User Registration**: Users are required to register with the bot, and their data is stored in **MongoDB Atlas**.

## Technologies Used
- **Python**: Main programming language for building the bot.
- **Telegram API**: For creating and managing the bot.
- **Gemini API**: For handling advanced natural language queries.
- **MongoDB Atlas**: Cloud database to store user information.
- **PyTesseract**: For Optical Character Recognition (OCR) to process images.
- **PyPDF2**: To extract text from PDF files.
- **VADER (NLTK) & TextBlob**: For performing **sentiment analysis** on user messages.
- **SerpAPI**: To perform web searches and fetch search results.
- **GitHub Actions**: For deployment and automation.

## How I Built It

1. **Set up the Telegram Bot**:
    - Created a bot on Telegram using BotFather.
    - Used the Python `python-telegram-bot` library to build the bot.

2. **Image and PDF Analysis**:
    - Used **PyTesseract** to extract text from images.
    - Used **PyPDF2** to extract text from PDF files.

3. **Sentiment Analysis**:
    - Implemented **VADER (NLTK)** and **TextBlob** to analyze user messages.
    - The bot responds differently based on the sentiment detected (positive, negative, neutral).

4. **Database Setup**:
    - Integrated **MongoDB Atlas** to store user data and preferences.
    - Implemented a registration system for users to sign up and store their information.

5. **Web Search Integration**:
    - Integrated **SerpAPI** to perform web searches and return relevant results to users.

6. **Error Handling**:
    - Added error handling and debugging features to ensure smooth operation and handle edge cases.

7. **Deployment**:
    - Deployed the bot using GitHub and GitHub Actions for continuous integration and deployment.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/shaikmohammadyasen/My_Telegram_AI_ChatBot.git
   ```

2. Navigate into the project directory:
   ```bash
   cd My_Telegram_AI_ChatBot
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for the Telegram Bot token and MongoDB credentials.

5. Run the bot:
   ```bash
   python main.py
   ```

## Contributions

Feel free to fork this repository and create pull requests for any improvements or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
