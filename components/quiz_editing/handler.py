from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from components.about.handler import tell_about_yourself
from components.interests.handler import ask_interests
from components.location.handler import ask_location
from constants.quiz_responses import QuizResponses
from modules.Quiz import Quiz
from utils import say_welcome
from utils.editing import set_editing_field


async def name_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponses.name
        set_editing_field(editing_field, globalState)
    await say_welcome(call.message, state)


async def location_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponses.location
        set_editing_field(editing_field, globalState)
    await ask_location(call.message, state)


async def about_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponses.about
        set_editing_field(editing_field, globalState)
    await tell_about_yourself(call.message, state)


async def interests_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponses.interests
        set_editing_field(editing_field, globalState)
    await Quiz.editing_interests.set()
    await ask_interests(call.message, state)
