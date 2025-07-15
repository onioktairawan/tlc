from telegram import Update
from telegram.ext import CallbackContext
from core import send_to_discord

def handle_telegram_reply(update: Update, context: CallbackContext):
    query = update.callback_query
    if not query:
        return
    context.user_data["discord_reply_to"] = query.data
    query.answer()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Silakan balas pesan ini untuk membalas ke Discord.",
        reply_to_message_id=query.message.message_id,
    )

async def handle_reply(update: Update, context: CallbackContext):
    if "discord_reply_to" in context.user_data:
        reply_to_id = int(context.user_data.pop("discord_reply_to"))
        await send_to_discord(reply_to_id, update.message.text)
        await update.message.reply_text("✅ Pesan dikirim ke Discord.")
