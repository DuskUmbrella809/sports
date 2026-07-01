from dotenv import load_dotenv
import os

load_dotenv()

API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")

if not API_FOOTBALL_KEY:
    raise RuntimeError("API_FOOTBALL_KEY is missing from .env")