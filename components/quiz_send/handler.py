from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from components.quiz_edit.keyboard import ikb_menu
from components.preview.keyboard_text import KeyboardText
from constants.message import MESSAGES
from modules.Quiz import Quiz
from utils import get_invite_link, send_user_data, clear_user_history


async def default(call: CallbackQuery, state: FSMContext):
    invite_link = await get_invite_link(state)
    if call.data == KeyboardText.send:
        await call.message.answer(
            MESSAGES.invite_link.substitute(
                invite_link=invite_link
            )
        )
    else:
        message_answer = await call.message.edit_text(
            MESSAGES.choose_edit_step,
            parse_mode="HTML"
        )
        await call.message.edit_reply_markup(
            reply_markup=ikb_menu
        )
        async with state.proxy() as globalState:
            globalState["_message"] = message_answer
        await Quiz.quiz_edit.set()
        return

    await send_user_data(state)
    await clear_user_history(state)

    await call.message.delete()
    await state.finish()
