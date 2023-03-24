from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from constants.message import MESSAGES
from constants.quiz_responses_fields import QuizResponsesFields
from utils import get_invite_link, send_user_data, clear_user_history_and_state
from utils.clear_user_history import delete_message


async def default(call: CallbackQuery, state: FSMContext):
    invite_link = await get_invite_link(state)
    message_answer = await call.message.answer(
        MESSAGES.invite_link.substitute(
            invite_link=invite_link
        ),
        parse_mode="HTML"
    )
    async with state.proxy() as quiz_responses:
        quiz_responses[QuizResponsesFields.last_message_id] = message_answer.message_id

    await send_user_data(state)
    await delete_message(call.message)
    await clear_user_history_and_state(state)

    await state.finish()
