from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_send = KeyboardButton('Отправить анкету')
button_edit = KeyboardButton('Редактировать')


quiz_preview = ReplyKeyboardMarkup(resize_keyboard=True)
quiz_preview.add(button_send)
quiz_preview.add(button_edit)
