import os
from telegram.ext import Application, MessageHandler, filters, CallbackQueryHandler
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv
from bridge import send_to_discord

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

tg_bot = Application.builder().token(TELEGRAM_TOKEN).build()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == int(TELEGRAM_CHAT_ID):
        await send_to_discord(update.message)

def run_telegram():
    tg_bot.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    return tg_bot.run_polling()
