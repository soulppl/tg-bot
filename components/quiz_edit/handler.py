from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from components.quiz_edit.keyboard import ikb_menu
from constants.message import MESSAGES
from constants.quiz_responses import QuizResponses
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state: FSMContext):
    message_answer = await call.message.edit_text(
        MESSAGES.choose_edit_step,
        parse_mode="HTML"
    )
    await call.message.edit_reply_markup(
        reply_markup=ikb_menu
    )
    async with state.proxy() as globalState:
        globalState[QuizResponses.service_data.last_message] = message_answer
    await Quiz.editing.set()
    return
