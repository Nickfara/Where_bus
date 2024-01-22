import logging
from aiogram import Bot, Dispatcher, types
import g4f
from aiogram.utils import executor
from Транспорт import program
# Включите логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
API_TOKEN = '6935521965:AAGCJPcCUUC-5KpNBwV0B69ojUZ7xf3IAcs'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Словарь для хранения истории разговоров
conversation_history = {}

# Функция для обрезки истории разговора
def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


@dp.message_handler(commands=['clear'])
async def process_clear_command(message: types.Message):
    user_id = message.from_user.id
    conversation_history[user_id] = [
            {
                "role": "user",
                "content": "Если я спрошу у тебя где трамвай, тебе нужно будет узнать у меня сначала куда я еду, а потом узнать нужный мне трамвай. Но если я тебе сразу скажу в какую сторону или номер трамвая, ты это запомни, и можешь не спрашивать! Когда у тебя будет вся информация, тебе нужно будет ответить следующим строго образом: [000]/Номер трамвая/ID остановки. Только одно условие, ты должен знать это остановку! А их всего 3: 3438 - это если я еду на домой или спрашиваю про остановку 'Театр Музыкальной комедии' и попросил 18 трамвай, 3457 - а это если я еду на работу или назвал остановку 'Студенческая' и попросил 18 трамвай, 3382 - это если я еду домой но попросил 4-й трамвай или назвал остановку 'Киностудия' или 'оперный театр'. Не в коем случае не добавляй вначале: [000], если у тебя нет чёткого номера трамвая из двух цифр, и нет чёкого id из тех, которые я тебе перечислил!"
            },
            {
                "role": "assistant",
                "content": "Хорошо! Давайте попробуем это сделать!"
            },
            {
                "role": "user",
                "content": "Давай! Где мой трамвай?"
            },
            {
                "role": "assistant",
                "content": "А куда ты едешь?"
            },
            {
                "role": "user",
                "content": "Домой"
            },
            {
                "role": "assistant",
                "content": "А какой трамвай тебе нужен?"
            },
            {
                "role": "user",
                "content": "18"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Давай потренеруемся ещё раз. Где мой трамвай?"
            },
            {
                "role": "assistant",
                "content": "А куда тебе нужно?"
            },
            {
                "role": "user",
                "content": "Домой"
            },
            {
                "role": "assistant",
                "content": "А какой трамвай нужен?"
            },
            {
                "role": "user",
                "content": "4"
            },
            {
                "role": "assistant",
                "content": "[000]/4/3382"
            },
            {
                "role": "user",
                "content": "Давай ещё потренеруемся!: Когда будет трамвай в сторону дома?"
            },
            {
                "role": "assistant",
                "content": "А какой трамвай нужен?"
            },
            {
                "role": "user",
                "content": "18"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Давай ещё потренеруемся!: Мне нужен 18 трамвай?"
            },
            {
                "role": "assistant",
                "content": "А куда ты направляешься?"
            },
            {
                "role": "user",
                "content": "Домой!"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Давай ещё потренеруемся!:Когда 18 трамвай будет в сторону дома?"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Супер! Всегда, когда я спрашиваю про местанахождение трамвая, отвечай примерно похожие ответы."
            },

        ]
    await message.reply("История диалога очищена.")

# Обработчик для каждого нового сообщения
@dp.message_handler()
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_input = message.text

    if user_id not in conversation_history:
        conversation_history[user_id] = [
            {
                "role": "user",
                "content": "Если я спрошу у тебя где трамвай, тебе нужно будет узнать у меня сначала куда я еду, а потом узнать нужный мне трамвай. Но если я тебе сразу скажу в какую сторону или номер трамвая, ты это запомни, и можешь не спрашивать! Когда у тебя будет вся информация, тебе нужно будет ответить следующим строго образом: [000]/Номер трамвая/ID остановки. Только одно условие, ты должен знать это остановку! А их всего 3: 3438 - это если я еду на домой или спрашиваю про остановку 'Театр Музыкальной комедии' и попросил 18 трамвай, 3457 - а это если я еду на работу или назвал остановку 'Студенческая' и попросил 18 трамвай, 3382 - это если я еду домой но попросил 4-й трамвай или назвал остановку 'Киностудия' или 'оперный театр'. Не в коем случае не добавляй вначале: [000], если у тебя нет чёткого номера трамвая из двух цифр, и нет чёкого id из тех, которые я тебе перечислил!"
            },
            {
                "role": "assistant",
                "content": "Хорошо! Давайте попробуем это сделать!"
            },
            {
                "role": "user",
                "content": "Давай! Где мой трамвай?"
            },
            {
                "role": "assistant",
                "content": "А куда ты едешь?"
            },
            {
                "role": "user",
                "content": "Домой"
            },
            {
                "role": "assistant",
                "content": "А какой трамвай тебе нужен?"
            },
            {
                "role": "user",
                "content": "18"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Давай потренеруемся ещё раз. Где мой трамвай?"
            },
            {
                "role": "assistant",
                "content": "А куда тебе нужно?"
            },
            {
                "role": "user",
                "content": "Домой"
            },
            {
                "role": "assistant",
                "content": "А какой трамвай нужен?"
            },
            {
                "role": "user",
                "content": "4"
            },
            {
                "role": "assistant",
                "content": "[000]/4/3382"
            },
            {
                "role": "user",
                "content": "Давай ещё потренеруемся!: Когда будет трамвай в сторону дома?"
            },
            {
                "role": "assistant",
                "content": "А какой трамвай нужен?"
            },
            {
                "role": "user",
                "content": "18"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Давай ещё потренеруемся!: Мне нужен 18 трамвай?"
            },
            {
                "role": "assistant",
                "content": "А куда ты направляешься?"
            },
            {
                "role": "user",
                "content": "Домой!"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Давай ещё потренеруемся!:Когда 18 трамвай будет в сторону дома?"
            },
            {
                "role": "assistant",
                "content": "[000]/18/3438"
            },
            {
                "role": "user",
                "content": "Супер! Всегда, когда я спрашиваю про местанахождение трамвая, отвечай примерно похожие ответы."
            },

        ]

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]

    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=chat_history,
            provider=g4f.Provider.GeekGpt,
            proxy="http://66.228.47.125:110"
        )
        chat_gpt_response = response
    except Exception as e:
        print(f"{g4f.Provider.GeekGpt.__name__}:", e)
        chat_gpt_response = "Извините, произошла ошибка."


    conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
    length = sum(len(message["content"]) for message in conversation_history[user_id])
    print(length)
    response_split = chat_gpt_response.split('/')
    print(chat_gpt_response)
    print(response_split)
    if response_split[0] == '[000]':
        await message.answer(program(response_split[1], response_split[2]))
    else:
        await message.answer(chat_gpt_response)



# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)