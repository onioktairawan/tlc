# handlers.py
from discord_listener import send_to_discord

def handle_telegram_reply(update, context):
    query = update.callback_query
    if not query:
        return
    message = query.message
    user = query.from_user
    original_discord_message_id = query.data

    context.bot.send_message(
        chat_id=message.chat_id,
        text=f"Silakan balas pesan ini untuk membalas ke Discord.",
        reply_to_message_id=message.message_id,
    )

    context.user_data["discord_reply_to"] = original_discord_message_id
    query.answer()
