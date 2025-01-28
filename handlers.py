from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Application, CallbackContext
from telegram.ext import filters  # Используем filters для фильтров команд

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Новости", url="https://OporaApp.ya79.repl.co/news")],
        [InlineKeyboardButton("Лекции", url="https://OporaApp.ya79.repl.co/lectures")],
        [InlineKeyboardButton("Тесты", url="https://OporaApp.ya79.repl.co/tests")],
        [InlineKeyboardButton("Календарь", url="https://OporaApp.ya79.repl.co/calendar")],
        [InlineKeyboardButton("Контакты", url="https://OporaApp.ya79.repl.co/contacts")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# Команда /help
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Команды:\n/start - Начало работы\n/help - Помощь')

# Обработка неизвестных команд
async def unknown(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Извините, я не понимаю эту команду.')

# Регистрируем обработчики для приложения
def setup_dispatcher(application: Application) -> None:
    # Добавляем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))
    # Добавляем обработчик для команды /help
    application.add_handler(CommandHandler("help", help_command))
    # Добавляем обработчик для неизвестных команд
    application.add_handler(MessageHandler(filters.Command(), unknown))  # Используем filters.Command() для перехвата всех команд
