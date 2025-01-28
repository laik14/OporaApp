import asyncio
from flask import Flask, render_template
from telegram.ext import Application
from config import TELEGRAM_BOT_TOKEN
from handlers import setup_dispatcher  # Импорт функции setup_dispatcher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/lectures')
def lectures():
    return render_template('lectures.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

# Функция для настройки бота
async def setup_bot():
    try:
        # Создаем объект Application с токеном
        application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

        # Регистрируем обработчики
        setup_dispatcher(application)

        # Запуск бота с Long Polling
        await application.run_polling()

    except Exception as e:
        print(f"Error while setting up the bot: {e}")

# Запуск приложения Flask и бота
async def main():
    # Запускаем бота в цикле событий
    bot_task = asyncio.create_task(setup_bot())

    # Запуск Flask на порту 80
    app.run(host="0.0.0.0", port=80, use_reloader=False)  # Используем порт 80 для публичного доступа

    await bot_task  # Ожидаем завершения задачи бота

if __name__ == '__main__':
    asyncio.run(main())  # Запуск всего приложения
