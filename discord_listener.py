import os
import discord
from dotenv import load_dotenv
from core import discord_messages
from bridge import send_to_telegram

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Untuk userbot (discord.py-self), tidak ada intents
client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f"[Discord] Logged in as {client.user} ({client.user.id})")

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return  # Abaikan pesan dari diri sendiri

    discord_messages[message.id] = message  # Simpan pesan
    await send_to_telegram(message.id, message.author.name, message.content)

async def run_discord():
    await client.start(DISCORD_TOKEN)
