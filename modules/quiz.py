from aiogram.dispatcher.filters.state import State, StatesGroup


class Quiz(StatesGroup):
    name = State()
    location = State()
    interests = State()
    who_am_i = State()

