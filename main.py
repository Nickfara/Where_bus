import os
from background import keep_alive #импорт функции для поддержки работоспособности
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
from Транспорт import program
import json
from GPT import GPT

stations = {}

with open("Остановки траллейбусы.json", "r") as json_station:
    station = json.load(json_station)
    stations['Траллейбусы'] = station
    print(str(len(station)) + ' траллейбусных остановок в ФАЙЛЕ!')

with open("Остановки трамваи.json", "r") as json_station:
    station = json.load(json_station)
    stations['Трамваи'] = station
    print(str(len(station)) + ' трамвайных остановок в ФАЙЛЕ!')

print(stations)

bot = telebot.TeleBot('6935521965:AAGCJPcCUUC-5KpNBwV0B69ojUZ7xf3IAcs')
data = []
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    check = GPT('Содержит ли следующее сообщение вопрос о местанахождении трамвая. Ответь только да или нет.: \n' + str(message).lower())
    print('check = ' + str(check))
    if check == 'да' or check == 'да.' or check == 'да!':
        if message.text == '/start':
            bot.send_message(message.from_user.id, 'Привет, напиши номер трамвая.')
        elif str(message.text) == '18':
            data.append(str(message.text))
            bot.send_message(message.from_user.id, 'Теперь, напиши остановку.')
        elif str(message.text).lower() == 'театр':
            data.append('3438')
            text = (str(data[0]), str(data[1]))
            bot.send_message(message.from_user.id, program(number=data[0], station=data[1]))
    else:
        bot.send_message(message.from_user.id, GPT(message))

keep_alive()
bot.polling(none_stop=True, interval=0)