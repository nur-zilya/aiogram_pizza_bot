from aiogram import types, Dispatcher
import json, string
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    #создаем множество, в котором проверяем сообщение пользователя на маты,
    # учитывая, что они могли быть зашифрованы с помощью пунктуации и др. символов, если находим
    # пересечения в сообщении и нашем списке, вывод предупреждения и удаление
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Swearing is prohibited!!!')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
