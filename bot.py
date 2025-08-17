import logging
import requests
import random
import os
import logging
import requests
import random
import os
from telegram.ext import Updater, CommandHandler

# =======================
# CONFIGURATION
# =======================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # <-- Render will provide this

# Some meme subreddits
SUBREDDITS = [
    "memes",
    "dankmemes",
    "wholesomememes",
    "AdviceAnimals",
    "me_irl",
    "historymemes",
]

# =======================
# LOGGING
# =======================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# =======================
# FUNCTIONS
# =======================
def get_random_meme():
    subreddit = random.choice(SUBREDDITS)
    url = f"https://meme-api.com/gimme/{subreddit}"
    try:
        response = requests.get(url).json()
        return response["url"], response["title"]
    except Exception as e:
        logging.error(f"Error fetching meme: {e}")
        return None, None


def send_meme(update, context):
    meme_url, title = get_random_meme()
    if meme_url:
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=meme_url,
            caption=title
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Couldn't fetch meme, try again!"
        )

# =======================
# MAIN
# =======================
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN environment variable not set!")

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("meme", send_meme))

    print("🤖 Bot is running... Type /meme in Telegram to get memes!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
# =======================
# CONFIGURATION
# =======================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # <-- use environment variable

# Some meme subreddits
SUBREDDITS = [
    "memes",
    "dankmemes",
    "wholesomememes",
    "AdviceAnimals",
    "me_irl",
    "historymemes",
]

# =======================
# LOGGING
# =======================
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# =======================
# FUNCTIONS
# =======================
def get_random_meme():
    subreddit = random.choice(SUBREDDITS)
    url = f"https://meme-api.com/gimme/{subreddit}"
    try:
        response = requests.get(url).json()
        return response["url"], response["title"]
    except Exception as e:
        logging.error(f"Error fetching meme: {e}")
        return None, None


def send_meme(update, context):
    meme_url, title = get_random_meme()
    if meme_url:
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=meme_url,
                               caption=title)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Couldn't fetch meme, try again!")

# =======================
# MAIN
# =======================
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN environment variable not set!")
    
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("meme", send_meme))

    print("🤖 Bot is running... Type /meme in Telegram to get memes!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    except Exception as e:
        logging.error(f"Error fetching meme: {e}")
        return None, None


def send_meme(update, context):
    meme_url, title = get_random_meme()
    if meme_url:
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=meme_url,
                               caption=title)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Couldn't fetch meme, try again!")

# =======================
# MAIN
# =======================
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN environment variable not set!")
    
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("meme", send_meme))

    print("🤖 Bot is running... Type /meme in Telegram to get memes!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()        logging.error(f"Error fetching meme: {e}")
        return None, None


def send_meme(update, context):
    meme_url, title = get_random_meme()
    if meme_url:
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=meme_url,
                               caption=title)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Couldn't fetch meme, try again!")

# =======================
# MAIN
# =======================
def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("meme", send_meme))

    print("🤖 Bot is running... Type /meme in Telegram to get memes!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()# MAIN
# =======================
def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("meme", send_meme))

    # Start polling
    print("🤖 Bot is running... Type /meme in Telegram to get memes!")
    updater.start_polling()
    updater.idle()

main()
