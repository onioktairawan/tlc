import discord
from discord import Message
from dotenv import load_dotenv
import os
from bridge import send_to_telegram

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"[Discord] Logged in as {client.user}")

@client.event
async def on_message(message: Message):
    if message.author.bot: return
    content = message.content.strip()
    author = str(message.author)
    discord_msg_id = str(message.id)
    await send_to_telegram(author, content, discord_msg_id)

def run_discord():
    client.run(DISCORD_TOKEN, bot=False)
