from aiogram.dispatcher.filters.state import State, StatesGroup


class Quiz(StatesGroup):
    welcome = State()
    name = State()
    location = State()
    interests = State()
    travels = State()
    who_am_i = State()
    send_quiz = State()
    edit_quiz = State()

