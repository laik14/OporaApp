from flask import Flask, request
import telegram
from telegram.ext import Application
from config import TELEGRAM_BOT_TOKEN  # Убедитесь, что ваш токен хранится в config.py

app = Flask(__name__)

# Инициализация бота Telegram
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

@app.route('/webhook/<token>', methods=['POST'])
def webhook(token):
    # Проверка, что токен в URL соответствует ожидаемому
    if token != TELEGRAM_BOT_TOKEN:
        return 'Unauthorized', 403

    # Получаем данные от Telegram (обновление)
    update = telegram.Update.de_json(request.get_json(), bot)

    # Обработка обновлений
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.update_queue.put(update)

    # Ответ Telegram о том, что запрос был успешно обработан
    return 'OK', 200

if __name__ == '__main__':
    # Убедитесь, что Flask сервер работает на публичном порте
    app.run(debug=True, host="0.0.0.0", port=5000)
