from aiogram import types
from aiogram.types import CallbackQuery, Message, InputMediaPhoto

from projects.user_quiz.components.interests.keyboard import ikb_menu
from constants.quiz_responses_fields import QuizResponsesFields
from modules.Quiz import Quiz
from aiogram.dispatcher import FSMContext
from constants.message import MESSAGES
from utils.clear_user_history import delete_message


async def default(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as quiz_responses:
        location = call.data
        quiz_responses[QuizResponsesFields.location] = location
    await ask_interests(call.message, state)


async def ask_interests(message: Message, state: FSMContext):
    photo = open('./projects/user_quiz/components/interests/interests.jpg', 'rb')

    message_answer = await message.answer_photo(
        photo=photo,
        caption=MESSAGES.what_you_are_interesting,
        parse_mode="HTML",
        reply_markup=ikb_menu,
    )

    async with state.proxy() as globalState:
        globalState[QuizResponsesFields.service_data.last_message] = message_answer

    await delete_message(message)

    await Quiz.next()
