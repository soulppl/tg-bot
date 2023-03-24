from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from projects.user_quiz.components.location.keyboard_text import Countries


inline_keyboard = [
    [
        InlineKeyboardButton(text=Countries.armenia, callback_data=Countries.armenia),
        InlineKeyboardButton(text=Countries.belorussia, callback_data=Countries.belorussia),
        InlineKeyboardButton(text=Countries.vietnam, callback_data=Countries.vietnam),

    ],
    [
        InlineKeyboardButton(text=Countries.germany, callback_data=Countries.germany),
        InlineKeyboardButton(text=Countries.georgia, callback_data=Countries.georgia),
        InlineKeyboardButton(text=Countries.india, callback_data=Countries.india),
    ],
    [
        InlineKeyboardButton(text=Countries.indonesia, callback_data=Countries.indonesia),
        InlineKeyboardButton(text=Countries.spain, callback_data=Countries.spain),
        InlineKeyboardButton(text=Countries.italy, callback_data=Countries.italy),
    ],
    [
        InlineKeyboardButton(text=Countries.kazahstan, callback_data=Countries.kazahstan),
        InlineKeyboardButton(text=Countries.kyrgizia, callback_data=Countries.kyrgizia),
        InlineKeyboardButton(text=Countries.uae, callback_data=Countries.uae),
    ],
    [
        InlineKeyboardButton(text=Countries.poland, callback_data=Countries.poland),
        InlineKeyboardButton(text=Countries.portugal, callback_data=Countries.portugal),
        InlineKeyboardButton(text=Countries.russia, callback_data=Countries.russia),
    ],
    [
        InlineKeyboardButton(text=Countries.serbia, callback_data=Countries.serbia),
        InlineKeyboardButton(text=Countries.thailand, callback_data=Countries.thailand),
        InlineKeyboardButton(text=Countries.turkey, callback_data=Countries.turkey),
    ],
    [
        InlineKeyboardButton(text=Countries.ukraine, callback_data=Countries.ukraine),
        InlineKeyboardButton(text=Countries.finland, callback_data=Countries.finland),
        InlineKeyboardButton(text=Countries.french, callback_data=Countries.french),
    ],
    [
        InlineKeyboardButton(text=Countries.montenegro, callback_data=Countries.montenegro),
        InlineKeyboardButton(text=Countries.czechia, callback_data=Countries.czechia),
        InlineKeyboardButton(text=Countries.sri_lanka, callback_data=Countries.sri_lanka),
    ],
    [
        InlineKeyboardButton(text=Countries.other, callback_data=Countries.other),
    ]
]

ikb_menu = InlineKeyboardMarkup(row_width=3, inline_keyboard=inline_keyboard)



