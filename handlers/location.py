from aiogram.types import CallbackQuery

from modules.keyboards.inline.interests import ikb_menu
from modules.quiz import Quiz
from aiogram.dispatcher import FSMContext
from modules.dp import dp
from constants.message import MESSAGES


async def keyboard_message(call: CallbackQuery, state: FSMContext):
    await set_location(call, state)


async def set_location(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as quiz_responses:
        location = call.data
        quiz_responses["location"] = location
    async with state.proxy() as quiz_responses:
        if "is_editing" in quiz_responses:
            await Quiz.next()
    message_answer = await call.message.edit_text(
        MESSAGES.what_you_are_interesting,
        parse_mode="HTML"
    )
    await call.message.edit_reply_markup(
        reply_markup=ikb_menu
    )
    async with state.proxy() as globalState:
        globalState["_message"] = message_answer

    await Quiz.next()
