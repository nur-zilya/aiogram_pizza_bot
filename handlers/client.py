from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Bon Appetit', reply_markup=kb_client)  # direct messages
        await message.delete()
    except:
        await message.reply(
            'Communication with bot via direct messages, write to him: \nhttps://t.me/pet_project_pizza_bot')


# @dp.message_handler(commands=['Working_hours'])
async def pizza_open_comand(message: types.Message):
    await bot.send_message(message.from_user.id, 'Mon-Sun 9:00 am - 9:00 pm')


# @dp.message_handler(commands=['Location'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Profsouznaya street, 6')

@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


# @dp.message_handler()
# async def empty(message: types.Message):
#     await message.answer('There is no such command')
#     await message.delete()

# регистрация хэндлеров "вручную"
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_comand, commands=['Working_hours'])
    dp.register_message_handler(pizza_place_command, commands=['Location'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])
