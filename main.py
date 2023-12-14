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
    id = '0'
    id = GPT(str('Вот сообщение: "' + str(message.text) + '". Если в нём про трамвай, ответь "1". Если нет ответь "4"'))
    if id == '4':
        id = GPT(
            str('Вот сообщение: "' + str(message.text) + '". Если это число от 1 до 24, ответь "2". Если нет ответь "4"'))
    if id == '4':
        id = GPT(
            str('Вот сообщение: "' + str(message.text) + '". Если оно как-то связано с этим списком:' + stations['Трамваи'] + ' ответь "3". Если нет ответь "4"'))

    if id == '1':
        bot.send_message(message.from_user.id, 'Привет, напиши номер трамвая.')
    elif id == '2':
        data.append(str(message.text))
        bot.send_message(message.from_user.id, 'Теперь, напиши остановку.')
    elif id == '3':
        text = 'Помоги найти мне вот эту остановку: "' + str(message.text) + '", Вот в этом вот словаре от python!: \n"' + \
               str(stations['Трамваи']) + '\n То, что написано цифрами, это ключи, то, что словами, это остановки. Ответь в ответном сообщении только ключём от нужной остановки!, а если ты считаешь, что остановки там нет, то ответь только цифрой "0"'
        if text == '0':
            bot.send_message(message.from_user.id, 'Такой остановки нет в Екатеринбурге!')
        else:
            key_responce = GPT(text)
            data.append(key_responce)
            bot.send_message(message.from_user.id, program(number=data[0], station=data[1]))
    elif id == '4':
        bot.send_message(message.from_user.id, GPT(str(message.text)))
    else:
        bot.send_message(message.from_user.id, str(id))

keep_alive()
bot.polling(none_stop=True, interval=0)