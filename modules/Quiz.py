from aiogram.dispatcher.filters.state import State, StatesGroup


class Quiz(StatesGroup):
    location = State()
    interests = State()
    interests_with_skip = State()
    travels = State()
    about = State()
    preview = State()
    edit_or_send = State()
    editing = State()
