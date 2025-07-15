from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["bridge_bot"]
messages = db["messages"]

async def save_message(discord_id, telegram_id):
    messages.insert_one({"discord_id": discord_id, "telegram_id": telegram_id})

async def get_discord_id(telegram_reply_to_id):
    doc = messages.find_one({"telegram_id": telegram_reply_to_id})
    return doc["discord_id"] if doc else None
