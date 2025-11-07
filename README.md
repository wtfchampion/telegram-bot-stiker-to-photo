📌 Sticker to Image Bot

This is a simple Telegram bot built with Python and the pyTelegramBotAPI (telebot) library. When a user sends a sticker, the bot downloads it, saves it as an image (in webp or jpg format), sends it back as a photo, and then deletes the temporary file. Perfect for users who want to save stickers as regular images! 🎉

✏️ Features
⦁ Sticker Handling: Converts and sends any sticker as an image.
⦁ Welcome Message: Sends a brief explanation on /start.
⦁ Temporary Storage: Files are saved in the stickers_as_images folder and auto-deleted.
⦁ Format Support: Handles webp (default for stickers) and other extensions.

✏️ Requirements
⦁ Python 3.7+
⦁ Libraries: pyTelegramBotAPI (install with pip install pyTelegramBotAPI)

✏️ Installation and Setup
1. Get Bot Token: Create a new bot via @BotFather on Telegram and copy the token.
2. Edit the Code: Replace 'token bot here' in the API_TOKEN line with your token.
3. Run: Save the file (e.g., sticker_bot.py) and execute in terminal:
   
   python sticker_bot.py
   
   The bot will start polling for messages.

✏️ Usage
⦁ Find the bot on Telegram and send /start.
⦁ Send any sticker—the bot will reply with its image version right away.
⦁ The stickers_as_images folder is created automatically for temp files (if needed).

✏️ Notes
⦁ Security: Keep your token private (use environment variables like os.getenv('BOT_TOKEN') for better practice).
⦁ Error Handling: Download or delete failures are logged to console without crashing the bot.
⦁ Improvements: You could add support for animated/video stickers or permanent saving.
⦁ License: None (as specified—no restrictions on use or modification).
