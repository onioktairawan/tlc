import asyncio
from discord_listener import run_discord
from telegram_bot import run_telegram

async def main():
    loop = asyncio.get_event_loop()
    await asyncio.gather(
        loop.run_in_executor(None, run_discord),
        loop.run_in_executor(None, run_telegram)
    )

if __name__ == "__main__":
    asyncio.run(main())
