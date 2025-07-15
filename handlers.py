from telegram import Update
from telegram.ext import ContextTypes
from bridge import send_to_discord

# Handler untuk tombol inline balas dari Telegram ke Discord
async def handle_telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # WAJIB pakai await karena ini coroutine

    message_id = query.data

    # Ambil isi pesan balasan pengguna
    reply_text = (
        query.message.reply_to_message.text
        if query.message.reply_to_message
        else "Balasan kosong"
    )

    # Kirim ke Discord
    await send_to_discord(message_id, reply_text)

    # Kirim konfirmasi ke Telegram
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="✅ Balasan berhasil dikirim ke Discord."
    )
