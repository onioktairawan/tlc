import os
from pymongo import MongoClient
from dotenv import load_dotenv
import logging

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["bridge_db"]
collection = db["message_links"]

logging.basicConfig(level=logging.DEBUG)

def save_message(discord_id, telegram_id, channel_id):
    logging.debug(f"Menyimpan link pesan: Discord {discord_id} <=> Telegram {telegram_id}")
    collection.insert_one({
        "discord_id": discord_id,
        "telegram_id": telegram_id,
        "channel_id": channel_id
    })

def get_discord_message_id(telegram_id):
    doc = collection.find_one({"telegram_id": telegram_id})
    return doc["discord_id"] if doc else None
