import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Debugging (print first few characters of token to check if it's loaded)
print(f"Loaded Token: {TOKEN[:5]}...")  # Should print "75612..."