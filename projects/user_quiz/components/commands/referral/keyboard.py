from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from projects.user_quiz.components.commands.referral.keyboard_text import KeyboardText

inline_keyboard = [
    [
        InlineKeyboardButton(text=KeyboardText.get_ref_list, callback_data=KeyboardText.get_ref_list),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.close, callback_data=KeyboardText.close),
    ],
]


inline_keyboard_referral_list = [
    [
        InlineKeyboardButton(text=KeyboardText.back, callback_data=KeyboardText.back),
    ],
    [
        InlineKeyboardButton(text=KeyboardText.close, callback_data=KeyboardText.close),
    ],
]


ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard)
ikb_menu_referral_list = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard_referral_list)
