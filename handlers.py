from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from bot import ADMINS  # Убедитесь, что этот импорт добавлен

def start(update: Update, context: CallbackContext) -> None:
    # ...existing code...

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Команды:\n/start - Начало работы\n/help - Помощь')

def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Извините, я не понимаю эту команду.')

def setup_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
