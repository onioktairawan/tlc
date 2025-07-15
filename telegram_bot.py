from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os
from bridge import send_to_discord
from database import get_discord_id

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))

app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

pending_replies = {}

async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_msg_id = update.message.reply_to_message.message_id
    original_discord_id = get_discord_id(tg_msg_id)
    if original_discord_id:
        await send_to_discord(update.message.text, original_discord_id)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data.startswith("reply:"):
        original_id = data.split(":")[1]
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Balas pesan ini untuk mengirim ke Discord.",
            reply_to_message_id=query.message.message_id,
        )
        pending_replies[update.effective_chat.id] = original_id

def run_telegram():
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.REPLY & filters.TEXT, handle_reply))
    app.run_polling()
