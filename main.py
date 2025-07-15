import asyncio
from discord_listener import run_discord
from telegram_bot import run_telegram

async def main():
    await asyncio.gather(run_discord(), run_telegram())

if __name__ == "__main__":
    asyncio.run(main())
