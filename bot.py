import telebot
import requests
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот для получения и анализа изображений. Отправь фото для анализа изображения")

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    '''При отправке изображения, проводит его анализ'''
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")

    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

bot.polling()
