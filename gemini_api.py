import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def query_gemini(prompt):
    """Send a query to Gemini AI and return the response."""
    try:
        model = genai.GenerativeModel("gemini-pro")  # Load model
        response = model.generate_content(prompt)  # Correct method
        return response.text  # Extract text response
    except Exception as e:
        return f"Error: {e}"