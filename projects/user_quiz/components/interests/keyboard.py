from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from projects.user_quiz.components.interests.keyboard_text import KeyboardText

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
]


ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard)
