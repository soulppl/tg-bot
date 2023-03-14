from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from components.quiz_edit.keyboard import ikb_menu
from components.preview.keyboard_text import KeyboardText
from constants.message import MESSAGES
from modules.Quiz import Quiz
from utils import get_invite_link, send_user_data, clear_user_history_and_state
from utils.clear_user_history import delete_message


async def default(call: CallbackQuery, state: FSMContext):
    invite_link = await get_invite_link(state)
    await call.message.answer(
        MESSAGES.invite_link.substitute(
            invite_link=invite_link
        ),
        parse_mode="HTML"
    )

    await send_user_data(state)
    await delete_message(call.message)
    await clear_user_history_and_state(state)

    await state.finish()
