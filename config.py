import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
AUTHORIZED_USERS = os.getenv("AUTHORIZED_USERS", "").split(",")  # Список разрешенных пользователей
LOG_FILE = "logs/bot.log"
