from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from handlers import handle_telegram_reply, handle_reply

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CallbackQueryHandler(handle_telegram_reply))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))
