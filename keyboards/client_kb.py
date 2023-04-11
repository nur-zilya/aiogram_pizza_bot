from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Working_hours')
b2 = KeyboardButton('/Location')
b3 = KeyboardButton('/Menu')
b4 = KeyboardButton('Share your phone number', request_contact=True)
b5 = KeyboardButton('Share your location', request_location=True)

# one_time_keyboard=True клавиатура один раз только появляется
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# add buttons from the new line
kb_client.insert(b1).row(b2, b3, b4, b5)
