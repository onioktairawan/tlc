from discord.ext import commands
import discord
import logging
from dotenv import load_dotenv
import os
from bridge import send_to_telegram

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@client.event
async def on_ready():
    logging.debug(f"[DISCORD] Logged in as {client.user}")

@client.event
async def on_message(message):
    # Optional filter kalau mau skip bot:
    if message.author.bot:
        return

    logging.debug(f"[DISCORD] Pesan diterima dari {message.author.name}: {message.content}")
    await send_to_telegram(message)

def run_discord():
    client.run(DISCORD_TOKEN)
