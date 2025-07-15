from discord_listener import run_discord
from telegram_bot import run_telegram
import threading

if __name__ == "__main__":
    t1 = threading.Thread(target=run_discord)
    t2 = threading.Thread(target=run_telegram)
    t1.start()
    t2.start()
