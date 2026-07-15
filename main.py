import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

api = os.getenv("GEMINI_API_KEY")
print(api)