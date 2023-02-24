from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants.menu.edit_quiz import EditQuizSteps

inline_keyboard = [
    [
        InlineKeyboardButton(text=EditQuizSteps.name, callback_data=EditQuizSteps.name),
    ],
    [
        InlineKeyboardButton(text=EditQuizSteps.location, callback_data=EditQuizSteps.location),
    ],
    [
        InlineKeyboardButton(text=EditQuizSteps.who_am_i, callback_data=EditQuizSteps.who_am_i),
    ]
]


edit_quiz_ikb_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard, one_time_keyboard=True)
