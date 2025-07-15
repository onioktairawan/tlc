from telegram import Update
from telegram.ext import ContextTypes
from bridge import send_to_discord

async def handle_telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    discord_msg_id = query.data
    context.user_data["reply_to"] = discord_msg_id

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"✏️ Balas pesan untuk ID Discord: {discord_msg_id}\nKetik dan kirim pesanmu sekarang..."
    )

async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    if "reply_to" not in user_data:
        return

    discord_msg_id = user_data.pop("reply_to")
    reply_text = update.message.text

    await send_to_discord(discord_msg_id, reply_text)
    await update.message.reply_text("✅ Sudah dibalas ke Discord.")
