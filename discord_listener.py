import os
from discord.ext import commands
from dotenv import load_dotenv
from bridge import send_to_telegram

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = commands.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)
discord_client = bot  # untuk akses dari bridge.py

@bot.event
async def on_ready():
    print(f"[Discord] Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.id != bot.user.id:
        return
    if message.channel.type.name == "private" or message.guild:
        msg_id = f"{message.channel.id}-{message.id}"
        await send_to_telegram(str(message.author), message.content, msg_id)

def run_discord():
    return bot.start(DISCORD_TOKEN)
