
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from constants.message import MESSAGES
from projects.user_quiz.components.preview.keyboard import ikb_menu
from constants.quiz_responses_fields import QuizResponsesFields
from modules.Quiz import Quiz
from utils.clear_user_history import delete_cached_messages, delete_message
from utils.user import get_welcome_topic_text, get_preview_text


async def default(message: types.Message, state: FSMContext):
    await send_message(message, message.text, state)


async def callback(call: CallbackQuery, state: FSMContext):
    await send_message(call.message, call.data, state)


async def send_message(message: types.Message, message_text: str, state: FSMContext):
    async with state.proxy() as quiz_responses:
        if (
                QuizResponsesFields.service_data.is_editing in quiz_responses and
                quiz_responses[QuizResponsesFields.service_data.editing_field] == QuizResponsesFields.interests
        ):
            pass
        elif (
                QuizResponsesFields.service_data.is_editing in quiz_responses
        ):
            edited_text = message_text
            edited_field = quiz_responses[QuizResponsesFields.service_data.editing_field]
            quiz_responses[edited_field] = edited_text
        else:
            about = message_text
            quiz_responses[QuizResponsesFields.about] = about
        welcome_preview_text = get_preview_text(quiz_responses)

    message_answer = await message.answer(
        text=welcome_preview_text,
        reply_markup=ikb_menu,
        parse_mode="HTML"
    )

    await delete_message(message)
    await delete_cached_messages(state)

    async with state.proxy() as globalState:
        globalState[QuizResponsesFields.service_data.last_message] = message_answer

    await Quiz.edit_or_send.set()
