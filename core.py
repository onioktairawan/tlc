# core.py
from discord import Message

# Simpan dictionary semua pesan
discord_messages = {}

async def send_to_discord(original_id, text):
    from discord_listener import client  # imported only when needed

    msg = discord_messages.get(original_id)
    if msg and msg.channel:
        await msg.channel.send(f"✉️ Balasan dari Telegram:\n{text}")
