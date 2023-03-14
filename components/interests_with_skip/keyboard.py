from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from components.interests.keyboard_text import KeyboardText


inline_keyboard = [
    [
        InlineKeyboardButton(text=KeyboardText.info, callback_data=KeyboardText.info),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.colivings, callback_data=KeyboardText.colivings),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.travels, callback_data=KeyboardText.travels),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.meetings, callback_data=KeyboardText.meetings),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.skip, callback_data=KeyboardText.skip),
    ]
]

ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard)
