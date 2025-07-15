from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(getenv("MONGO_URI"))
db = client['bridge_db']
collection = db['message_links']

def save_message(discord_id, telegram_msg_id):
    collection.insert_one({"discord_id": discord_id, "telegram_msg_id": telegram_msg_id})

def get_discord_id(telegram_msg_id):
    doc = collection.find_one({"telegram_msg_id": telegram_msg_id})
    return doc['discord_id'] if doc else None
