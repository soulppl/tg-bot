from aiogram import types
from aiogram.dispatcher.filters import Filter

from projects.user_quiz.components.quiz_edit import KeyboardText
from constants import FiltersNames


class NameFilter(Filter):
    print('name filter')

    key = FiltersNames.name

    async def check(self, call: types.CallbackQuery):
        return call.data == KeyboardText.name


class LocationFilter(Filter):
    print('location filter')

    key = FiltersNames.location

    async def check(self, call: types.CallbackQuery):
        return call.data == KeyboardText.location


class InterestsFIlter(Filter):
    print('interests filter')

    key = FiltersNames.interests

    async def check(self, call: types.CallbackQuery):
        return call.data == KeyboardText.interests


class AboutFilter(Filter):
    print('about filter')

    key = FiltersNames.about

    async def check(self, call: types.CallbackQuery):
        return call.data == KeyboardText.about
