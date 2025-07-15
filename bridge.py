from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot import app
import os
from database import save_message

TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))

async def send_to_telegram(author, content, discord_msg_id):
    keyboard = [[InlineKeyboardButton("💬 Balas", callback_data=f"reply:{discord_msg_id}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = await app.bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=f"<b>{author}</b>:\n{content}",
        parse_mode="HTML",
        reply_markup=reply_markup
    )
    save_message(discord_msg_id, msg.message_id)

async def send_to_discord(reply_text, discord_msg_id):
    from discord_listener import client
    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                msg = await channel.fetch_message(int(discord_msg_id))
                await msg.reply(reply_text)
                return
            except Exception:
                continue
