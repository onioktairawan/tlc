from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackContext, MessageHandler, filters, CallbackQueryHandler, CommandHandler
import os
from dotenv import load_dotenv
from handlers import handle_telegram_reply

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Application.builder().token(TELEGRAM_TOKEN).build()

@app.message_handler(filters.TEXT & (~filters.COMMAND))
async def handle_reply(update: Update, context: CallbackContext):
    if "discord_reply_to" in context.user_data:
        from discord_listener import send_to_discord  # import di dalam fungsi untuk hindari circular import
        reply_to_id = context.user_data.pop("discord_reply_to")
        await send_to_discord(reply_to_id, update.message.text)
        await update.message.reply_text("Pesan sudah dikirim ke Discord.")

app.add_handler(CallbackQueryHandler(handle_telegram_reply))
