from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

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
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()