from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot import tg_bot, TELEGRAM_CHAT_ID
from database import save_message, get_discord_id
from discord_listener import discord_client

async def send_to_telegram(author, content, discord_msg_id):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("✉️ Balas", callback_data=f"reply:{discord_msg_id}")
    ]])
    sent_msg = await tg_bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=f"<b>{author}</b>\n{content}",
        parse_mode='HTML',
        reply_markup=keyboard
    )
    await save_message(discord_msg_id, sent_msg.message_id)

async def send_to_discord(telegram_msg):
    if telegram_msg.reply_to_message:
        replied_telegram_id = telegram_msg.reply_to_message.message_id
        discord_msg_id = await get_discord_id(replied_telegram_id)
        if discord_msg_id:
            try:
                discord_msg = await discord_client.get_channel(int(discord_msg_id.split('-')[0])).fetch_message(int(discord_msg_id.split('-')[1]))
                await discord_msg.reply(f"Reply from Telegram: {telegram_msg.text}")
            except Exception as e:
                print("Error replying to Discord:", e)
