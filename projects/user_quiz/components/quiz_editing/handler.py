from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from projects.user_quiz.components.about.handler import tell_about_yourself
from projects.user_quiz.components.interests.handler import ask_interests
from projects.user_quiz.components.location.handler import ask_location
from constants.quiz_responses_fields import QuizResponsesFields
from modules.Quiz import Quiz
from utils import say_welcome
from utils.editing import set_editing_field


async def name_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponsesFields.name
        set_editing_field(editing_field, globalState)
    await say_welcome(call.message, state)


async def location_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponsesFields.location
        set_editing_field(editing_field, globalState)
    await ask_location(call.message, state)


async def about_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponsesFields.about
        set_editing_field(editing_field, globalState)
    await tell_about_yourself(call.message, state)


async def interests_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        editing_field = QuizResponsesFields.interests
        set_editing_field(editing_field, globalState)
    await Quiz.editing_interests.set()
    await ask_interests(call.message, state)
