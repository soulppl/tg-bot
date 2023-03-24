from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.quiz_responses_fields import QuizResponsesFields
from modules.DP import bot
from modules.google_sheet.google_sheet import send_user_quiz_to_sheets
from utils.envs import get_forum_id, get_user_info_topic_id
from utils.user import get_info_google_doc, get_welcome_topic_text


async def send_user_data(state: FSMContext):
    forum_id = get_forum_id()
    user_info_topic_id = get_user_info_topic_id()
    async with state.proxy() as quiz_responses:
        quiz_responses.pop(QuizResponsesFields.service_data.last_message, None)
        quiz_responses.pop(QuizResponsesFields.service_data.editing_field, None)
        quiz_responses.pop(QuizResponsesFields.service_data.is_editing, None)

        user_info = get_info_google_doc(quiz_responses)

        await send_user_quiz_to_sheets(user_info)

        welcome_topic_text = get_welcome_topic_text(quiz_responses)
        await bot.send_message(
            chat_id=forum_id,
            message_thread_id=user_info_topic_id,
            text=welcome_topic_text,
            parse_mode="HTML"
        )