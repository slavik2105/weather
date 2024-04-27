import telebot
import requests
import json

bot = telebot.TeleBot('7141637029:AAF9vvRySH-7DkUhi4kM41e_YEQh0XXVjRk')
API = '7a508b5a2489bf92cb18e478c2b8ef8c'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        bot.reply_to(message, f'сейчас погода: {temp}°C' f'\nвлажность воздуха: {humidity}%'f'\nветер: {wind}м/с')

        image = 'hot.jpg' if temp > 20.0 and 30.0 else 'cold.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'город указан не верно')


bot.polling(none_stop=True)
