import asyncio
from telegram_bot import app
from discord_listener import run_discord

async def main():
    telegram_task = app.run_polling()
    discord_task = run_discord()
    await asyncio.gather(telegram_task, discord_task)

if __name__ == "__main__":
    asyncio.run(main())
