from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from constants.message import MESSAGES
from projects.user_quiz.components.about.keyboard import ikb_menu as ikb_menu_about_skip
from constants.quiz_responses_fields import QuizResponsesFields
from modules.Quiz import Quiz
from utils.clear_user_history import delete_message


async def default(call: CallbackQuery, state: FSMContext):
    await tell_about_yourself(call.message, state)


async def tell_about_yourself(message: types.Message, state: FSMContext):
    message_answer = await message.answer(
        MESSAGES.tell_about_yourself,
        reply_markup=ikb_menu_about_skip,
        parse_mode="HTML"
    )
    await delete_message(message)
    async with state.proxy() as globalState:
        globalState[QuizResponsesFields.service_data.last_message] = message_answer

    await Quiz.preview.set()

