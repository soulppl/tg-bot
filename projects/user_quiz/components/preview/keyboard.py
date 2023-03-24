from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from projects.user_quiz.components.preview.keyboard_text import KeyboardText

inline_keyboard = [
    [
        InlineKeyboardButton(text=KeyboardText.edit, callback_data=KeyboardText.edit),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.send, callback_data=KeyboardText.send),
    ]
]


ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard)
