from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, MessageHandler, filters, ContextTypes, CommandHandler
from database import get_discord_message_id
from bridge import reply_to_discord
import os
import logging
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

logging.basicConfig(level=logging.DEBUG)

pending_replies = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif.")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    telegram_msg_id = query.message.message_id
    logging.debug(f"[TELEGRAM] Tombol reply diklik untuk message ID: {telegram_msg_id}")

    pending_replies[query.from_user.id] = telegram_msg_id
    await query.message.reply_text("Ketik balasanmu:")

async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in pending_replies:
        telegram_msg_id = pending_replies.pop(user_id)
        reply_text = update.message.text
        logging.debug(f"[TELEGRAM] Balasan diterima: {reply_text}")
        await reply_to_discord(telegram_msg_id, reply_text)
        await update.message.reply_text("Sudah dibalas ke Discord.")

async def run_telegram():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
