import asyncio
from discord_listener import run_discord
from telegram_bot import run_telegram

async def main():
    # Jalankan dua bot secara bersamaan
    telegram_task = asyncio.create_task(run_telegram())
    discord_task = asyncio.create_task(run_discord())
    await asyncio.gather(telegram_task, discord_task)

if __name__ == "__main__":
    asyncio.run(main())
