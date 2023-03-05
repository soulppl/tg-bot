from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from components.travels.keyboard_text import Travels

inline_keyboard = [
    [
        InlineKeyboardButton(text=Travels.yes, callback_data=Travels.yes),
        InlineKeyboardButton(text=Travels.no, callback_data=Travels.no),

    ],
]


ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard)
