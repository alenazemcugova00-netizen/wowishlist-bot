import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Токен бота берётся из переменной окружения (ты добавишь его на Render)
TOKEN = os.getenv("TOKEN")

# 👋 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first = update.effective_user.first_name
    await update.message.reply_text(
        f"Привет, {user_first}! 🎁\n"
        "Я — WoWishlist Bot.\n"
        "Я помогу тебе создать вишлист для любого события!\n\n"
        "Скоро ты сможешь добавлять подарки и делиться списком с друзьями 💝"
    )

# 🧠 Главная функция
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
