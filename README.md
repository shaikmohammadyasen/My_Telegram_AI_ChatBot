# My_Telegram_AI_ChatBot

## Project Description

The "Telegram AI ChatBot" is an intelligent bot designed to interact with users via the Telegram platform. It integrates various technologies to offer multiple functionalities, including image and file processing, web search capabilities, and a referral system. This bot provides responses and performs analysis based on the user's queries and shared files. 

The bot is powered by the **Gemini API** for handling natural language queries, and **MongoDB Atlas** is used to store user data for better interaction and functionality.

## Features
- **Image Analysis**: The bot is capable of processing images and extracting text from them using OCR (Optical Character Recognition) techniques.
- **File Processing**: The bot can analyze PDF files and extract text for users.
- **Web Search**: Integrates with **SerpAPI** to fetch search results from the web.
- **User Registration**: Users are required to register with the bot, and their data is stored in **MongoDB Atlas**.
- **Referral System**: Users can refer others to the bot and get rewards/points.

## Technologies Used
- **Python**: Main programming language for building the bot.
- **Telegram API**: For creating and managing the bot.
- **Gemini API**: For handling advanced natural language queries.
- **MongoDB Atlas**: Cloud database to store user information.
- **PyTesseract**: For Optical Character Recognition (OCR) to process images.
- **PyPDF2**: To extract text from PDF files.
- **SerpAPI**: To perform web searches and fetch search results.
- **GitHub Actions**: For deployment and automation.

## How I Built It

1. **Set up the Telegram Bot**:
    - Created a bot on Telegram using BotFather.
    - Used the Python `python-telegram-bot` library to build the bot.

2. **Image and PDF Analysis**:
    - Used **PyTesseract** to extract text from images.
    - Used **PyPDF2** to extract text from PDF files.

3. **Database Setup**:
    - Integrated **MongoDB Atlas** to store user data and preferences.
    - Implemented a registration system for users to sign up and store their information.

4. **Web Search Integration**:
    - Integrated **SerpAPI** to perform web searches and return relevant results to users.

5. **Referral System**:
    - Designed and implemented a referral system where users can refer others to use the bot.

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

---

You can modify the content to match exactly what you've built, but this template covers the basics for a well-organized and informative README. Let me know if you'd like any adjustments!
