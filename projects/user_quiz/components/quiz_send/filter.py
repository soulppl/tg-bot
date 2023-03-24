from aiogram import types
from aiogram.dispatcher.filters import Filter

from projects.user_quiz.components.preview.keyboard_text import KeyboardText


class Filter(Filter):
    print('send filter')
    key = "is_sending"

    async def check(self, call: types.CallbackQuery):
        return call.data == KeyboardText.send
