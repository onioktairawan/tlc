from discord.ext import commands
import discord
import logging
from dotenv import load_dotenv
import os
from bridge import send_to_telegram

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Tidak menggunakan Intents karena discord.py-self tidak menyediakannya
client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_ready():
    logging.debug(f"[DISCORD] Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    logging.debug(f"[DISCORD] Pesan diterima dari {message.author.name}: {message.content}")
    await send_to_telegram(message)

async def run_discord():
    await client.start(DISCORD_TOKEN)
