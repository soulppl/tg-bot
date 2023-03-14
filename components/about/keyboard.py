from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.about.keyboard_text import KeyboardText

inline_keyboard = [
    [
        InlineKeyboardButton(text=KeyboardText.skip, callback_data=KeyboardText.skip),
    ],
]


ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard)
