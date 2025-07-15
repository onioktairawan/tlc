import asyncio
from telegram_bot import app
from discord_listener import run_discord

async def run_telegram():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # Jangan stop polling (biarkan terus berjalan)
    # await app.updater.idle()

async def main():
    telegram_task = asyncio.create_task(run_telegram())
    discord_task = asyncio.create_task(run_discord())
    await asyncio.gather(telegram_task, discord_task)

if __name__ == "__main__":
    asyncio.run(main())
