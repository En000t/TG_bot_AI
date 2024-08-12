from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from modules.text_generator import TextGenerator
from security.access_control import is_user_authorized
import config

# Создаем экземпляр TextGenerator
generator = TextGenerator()

# Обработка команды /start
def start(update: Update, context: CallbackContext):
    print("Команда /start была вызвана")  # Отладочный вывод
    if not is_user_authorized(update.message.from_user.id):
        update.message.reply_text("У вас нет доступа к этому боту.")
        return
    update.message.reply_text("Привет! Я бот для генерации текста. Используйте команду /generate для создания текста.")

# Обработка команды /generate
def generate_text(update: Update, context: CallbackContext):
    print("Команда /generate была вызвана")  # Отладочный вывод
    if not is_user_authorized(update.message.from_user.id):
        update.message.reply_text("У вас нет доступа к этому боту.")
        return

    prompt = ' '.join(context.args)
    if prompt:
        print(f"Генерация текста с промптом: {prompt}")  # Отладочный вывод
        text = generator.generate(prompt)
        update.message.reply_text(text)
    else:
        update.message.reply_text("Пожалуйста, введите текст для генерации после команды /generate.")

# Основная функция для запуска бота
def main():
    print("Запуск бота...")  # Отладочный вывод
    # Создаем Updater и регистрируем обработчики команд
    updater = Updater(config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("generate", generate_text))

    # Запускаем бота
    updater.start_polling()
    print("Бот запущен и ожидает команды")  # Отладочный вывод
    updater.idle()

if __name__ == '__main__':
    main()
