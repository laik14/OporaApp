from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters  # Добавьте недостающие импорты
from config import TELEGRAM_BOT_TOKEN, ADMINS
from handlers import setup_dispatcher

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Новости", web_app=WebAppInfo(url="http://localhost:5000/news"))],
        [InlineKeyboardButton("Лекции", web_app=WebAppInfo(url="http://localhost:5000/lectures"))],
        [InlineKeyboardButton("Тесты", web_app=WebAppInfo(url="http://localhost:5000/tests"))],
        [InlineKeyboardButton("Календарь", web_app=WebAppInfo(url="http://localhost:5000/calendar"))],
        [InlineKeyboardButton("Контакты", web_app=WebAppInfo(url="http://localhost:5000/contacts"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    setup_dispatcher(dispatcher)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()