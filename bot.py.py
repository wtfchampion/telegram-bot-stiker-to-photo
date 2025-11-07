import telebot
import os

API_TOKEN = 'token bot here'  # paste your bot token in here
bot = telebot.TeleBot(API_TOKEN)
#created by : @wtfchampion | in telegram and git
SAVE_DIR = 'stickers_as_images'
os.makedirs(SAVE_DIR, exist_ok=True)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Hello! 👋\n"
        "This bot will send you the sticker as an image when you send one.\n"
        "Just send a sticker and you'll get its photo version.\n"
        "Enjoy! 🎉"
    )
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_file_id = message.sticker.file_id
    file_info = bot.get_file(sticker_file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    file_ext = os.path.splitext(file_info.file_path)[-1] or '.webp'
    file_path = os.path.join(SAVE_DIR, f"{sticker_file_id}{file_ext}")

    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    with open(file_path, 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="استیکرت به صورت عکس")

    try:
        os.remove(file_path)
    except Exception as e:
        print(f"خطا در حذف فایل {file_path}: {e}")

print("Bot is running...")
bot.polling()
