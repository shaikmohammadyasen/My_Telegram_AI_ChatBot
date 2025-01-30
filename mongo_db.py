from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Retrieve Mongo URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
# Specify the database name (replace 'your_db_name' with the desired name for your database)
db = client['mohammadyasenshaik']  # Replace 'your_db_name' with the actual name you want to use
collection = db['chat_history']  # Collection name
user_collection = db['users']  # Users collection
file_metadata_collection = db['file_metadata']  # File metadata collection

# Function to store user data in MongoDB
def store_user_data(chat_id, first_name, username):
    try:
        user_data = {
            'chat_id': chat_id,
            'first_name': first_name,
            'username': username,
            'timestamp': datetime.now()
        }
        # Insert user data into MongoDB users collection
        user_collection.insert_one(user_data)
        print("User data stored successfully!")
    except Exception as e:
        print(f"Error storing user data: {e}")

# Function to check if the user is registered in MongoDB
def is_user_registered(chat_id):
    user = user_collection.find_one({'chat_id': chat_id})
    return user is not None

# Function to save user's phone number
def save_user_phone(chat_id, phone_number):
    try:
        user_collection.update_one(
            {'chat_id': chat_id},
            {'$set': {'phone_number': phone_number}},
            upsert=True
        )
        print("Phone number saved successfully!")
    except Exception as e:
        print(f"Error saving phone number: {e}")

# Function to store chat data in MongoDB
def store_chat_in_mongo(user_query, gemini_response, chat_id):
    try:
        chat_data = {
            'user_query': user_query,
            'gemini_response': gemini_response,
            'timestamp': datetime.now(),
            'chat_id': chat_id
        }
        # Insert chat data into the MongoDB collection
        collection.insert_one(chat_data)
        print("Chat data stored successfully!")
    except Exception as e:
        print(f"Error storing data: {e}")

# Function to store file metadata in MongoDB
def store_file_metadata(file_id, file_type, extracted_text, analysis, chat_id):
    try:
        file_metadata = {
            'file_id': file_id,
            'file_type': file_type,
            'extracted_text': extracted_text,
            'analysis': analysis,
            'timestamp': datetime.now(),
            'chat_id': chat_id
        }
        # Insert file metadata into the MongoDB collection
        file_metadata_collection.insert_one(file_metadata)
        print("File metadata stored successfully!")
    except Exception as e:
        print(f"Error storing file metadata: {e}")
