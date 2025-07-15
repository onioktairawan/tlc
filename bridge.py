from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram_bot import app, TELEGRAM_CHAT_ID

async def send_to_telegram(message_id, author_name, content):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Balas", callback_data=str(message_id))]
    ])
    await app.bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=f"👤 {author_name}:\n{content}",
        reply_markup=keyboard
    )
