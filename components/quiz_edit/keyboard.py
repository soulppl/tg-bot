from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.quiz_edit.keyboard_text import KeyboardText

inline_keyboard = [
    [
        InlineKeyboardButton(text=KeyboardText.name, callback_data=KeyboardText.name),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.location, callback_data=KeyboardText.location),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.about, callback_data=KeyboardText.about),
    ]
]


ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard, one_time_keyboard=True)
