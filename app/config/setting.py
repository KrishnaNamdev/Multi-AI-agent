from dotenv import load_dotenv
import os

load_dotenv()

class Setting:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES = [
        "llama3-70b-8192",
        "llama-3.3-70b-versatile",
    ]

settings = Setting()