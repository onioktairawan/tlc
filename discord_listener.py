# discord_listener.py
import os
import discord
from dotenv import load_dotenv
from core import discord_messages
from bridge import send_to_telegram

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    discord_messages[message.id] = message  # Simpan pesan
    await send_to_telegram(message.id, message.author.name, message.content)

async def run_discord():
    await client.start(DISCORD_TOKEN)
