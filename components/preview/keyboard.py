from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from components.preview.keyboard_text import KeyboardText

inline_keyboard = [
    [
        InlineKeyboardButton(text=KeyboardText.edit, callback_data=KeyboardText.edit),
        InlineKeyboardButton(text=KeyboardText.send, callback_data=KeyboardText.send),
    ],
]


ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard)
