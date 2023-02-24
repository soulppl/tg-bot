from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants.menu.quiz_preview import QuizPreview

inline_keyboard = [
    [
        InlineKeyboardButton(text=QuizPreview.edit, callback_data=QuizPreview.edit),
        InlineKeyboardButton(text=QuizPreview.send_quiz, callback_data=QuizPreview.send_quiz),
    ],
]


ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard)
