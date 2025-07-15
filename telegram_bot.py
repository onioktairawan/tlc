import os
from telegram.ext import Application, CallbackQueryHandler, MessageHandler, filters
from dotenv import load_dotenv
from handlers import handle_telegram_reply, handle_reply
from bridge import set_bot

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "0"))

app = Application.builder().token(TELEGRAM_TOKEN).build()

# Set bot ke bridge
set_bot(app.bot, TELEGRAM_CHAT_ID)

app.add_handler(CallbackQueryHandler(handle_telegram_reply))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))
