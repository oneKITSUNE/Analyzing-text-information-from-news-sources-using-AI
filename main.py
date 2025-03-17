import telebot
from telebot import types
import requests

# Подключение бота Telegram
API_TOKEN = '7132690600:AAFGLf6GlkklcE12lr3De7sNqejJqfKVctY'
bot = telebot.TeleBot(API_TOKEN)

# Ключ авторизации для GigaChat
GIGA_CHAT_API_KEY = "MWExNzJmYzYtOWEzNi00NWFkLTg2YzQtMmFkMTUyMTQ0YjdiOjFiYTc1YzU2LTExYjYtNGI2Mi1iMDY3LTI2MDQ1Mjc0NDFhYw=="  # Используйте свой ключ

# Приветствие и кнопки для перехода на сайты
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Тасс")
    item2 = types.KeyboardButton("РИА Новости")
    item3 = types.KeyboardButton("Дзен")
    item4 = types.KeyboardButton("Хотите загрузить файл TXT?")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Привет! Я готов помочь тебе с анализом новостей. Выберите одну из опций:", reply_markup=markup)

# Обработка кнопок
@bot.message_handler(func=lambda message: message.text in ['Тасс', 'РИА Новости', 'Дзен'])
def handle_website(message):
    if message.text == 'Тасс':
        bot.send_message(message.chat.id, "Переход на ТАСС: [ТАСС](https://tass.ru/)", parse_mode='Markdown')
    elif message.text == 'РИА Новости':
        bot.send_message(message.chat.id, "Переход на РИА Новости: [РИА Новости](https://ria.ru/)", parse_mode='Markdown')
    elif message.text == 'Дзен':
        bot.send_message(message.chat.id, "Переход на Дзен: [Дзен](https://dzen.ru/)", parse_mode='Markdown')

# Обработка кнопки загрузки файла
@bot.message_handler(func=lambda message: message.text == "Хотите загрузить файл TXT?")
def ask_for_file(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item_yes = types.KeyboardButton("Да")
    item_no = types.KeyboardButton("Нет")
    markup.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Хотите загрузить файл TXT?", reply_markup=markup)

# Запрос на загрузку файла
@bot.message_handler(func=lambda message: message.text == "Да")
def request_file(message):
    bot.send_message(message.chat.id, "Пожалуйста, пришлите ваш файл TXT")

# Обработка полученного файла
@bot.message_handler(content_types=['document'])
def handle_document(message):
    # Скачиваем файл
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file_url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file_info.file_path}"

    # Скачиваем файл и читаем содержимое
    download_file(file_url, message.document.file_name)

    # Чтение файла и анализ через GigaChat
    news_text = read_file_with_correct_encoding(message.document.file_name)
    analysis = analyze_news_with_gigachat(news_text)

    # Отправляем результаты анализа пользователю
    bot.reply_to(message, analysis)

# Функция для скачивания файла
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Функция для чтения файла с автоматическим определением кодировки
def read_file_with_correct_encoding(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Интеграция с GigaChat для анализа текста
def analyze_news_with_gigachat(news_text):
    url = "https://gigachat.devices.sberbank.ru/"
    headers = {
        'Authorization': f'Bearer {GIGA_CHAT_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        "text": news_text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        analysis = f"Результаты анализа с GigaChat:\n\n{result['analysis']}"
    else:
        analysis = "Произошла ошибка при анализе текста с GigaChat."
    return analysis

# Запуск бота
bot.polling()
print ("test")