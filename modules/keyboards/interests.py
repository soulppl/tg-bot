from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants.menu.interests import Interests


inline_keyboard = [
    [
        InlineKeyboardButton(text=Interests.travels, callback_data=Interests.travels),
        InlineKeyboardButton(text=Interests.meetings, callback_data=Interests.meetings),
    ],
    [
        InlineKeyboardButton(text=Interests.info, callback_data=Interests.info),
        InlineKeyboardButton(text=Interests.colivings, callback_data=Interests.colivings),
    ]
]


inline_keyboard_with_skip = [
    [
        InlineKeyboardButton(text=Interests.travels, callback_data=Interests.travels),
        InlineKeyboardButton(text=Interests.meetings, callback_data=Interests.meetings),
    ],
    [
        InlineKeyboardButton(text=Interests.info, callback_data=Interests.info),
        InlineKeyboardButton(text=Interests.colivings, callback_data=Interests.colivings),
    ],
    [
        InlineKeyboardButton(text=Interests.skip, callback_data=Interests.skip),
    ]
]

ikb_menu = InlineKeyboardMarkup(row_width=3, inline_keyboard=inline_keyboard)
ikb_menu_with_skip = InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard_with_skip)
