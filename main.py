from telegram_bot import app
from discord_listener import run_discord
import asyncio

async def main():
    # Jalankan Discord listener di task terpisah
    discord_task = asyncio.create_task(run_discord())

    # Jalankan Telegram polling di thread terpisah agar tidak bentrok event loop
    from threading import Thread
    Thread(target=app.run_polling, daemon=True).start()

    # Tunggu task Discord berjalan terus-menerus
    await discord_task

if __name__ == "__main__":
    asyncio.run(main())
