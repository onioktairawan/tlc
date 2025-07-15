from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
import logging
from database import save_message, get_discord_message_id
import discord

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_to_telegram(message: discord.Message):
    nama = message.author.name
    isi = message.content
    tombol = InlineKeyboardMarkup([[InlineKeyboardButton("Balas", callback_data="reply")]])

    kirim = await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=f"<b>{nama}</b>:\n{isi}",
        parse_mode="HTML",
        reply_markup=tombol
    )

    logging.debug(f"[BRIDGE] Mengirim pesan dari Discord ke Telegram: {isi}")
    save_message(str(message.id), kirim.message_id, str(message.channel.id))

async def reply_to_discord(telegram_msg_id, reply_text):
    from discord_listener import client  # Hindari circular import

    discord_msg_id = get_discord_message_id(telegram_msg_id)
    if not discord_msg_id:
        logging.warning(f"[BRIDGE] Tidak ditemukan link untuk Telegram ID {telegram_msg_id}")
        return

    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                msg = await channel.fetch_message(int(discord_msg_id))
                await msg.reply(reply_text)
                logging.debug(f"[BRIDGE] Mengirim balasan ke Discord: {reply_text}")
                return
            except Exception as e:
                continue
