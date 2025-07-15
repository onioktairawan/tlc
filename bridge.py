TELEGRAM_BOT = None
TELEGRAM_CHAT_ID = None

def set_bot(bot, chat_id):
    global TELEGRAM_BOT, TELEGRAM_CHAT_ID
    TELEGRAM_BOT = bot
    TELEGRAM_CHAT_ID = chat_id

async def send_to_telegram(discord_msg_id, author_name, content):
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup

    if not TELEGRAM_BOT:
        print("Telegram bot belum diset.")
        return

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️ Balas", callback_data=str(discord_msg_id))]
    ])

    await TELEGRAM_BOT.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=f"💬 Pesan dari *{author_name}*:\n\n{content}",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def send_to_discord(discord_msg_id, reply_text):
    from core.discord_messages import discord_messages

    message = discord_messages.get(int(discord_msg_id))
    if message:
        await message.reply(reply_text)
