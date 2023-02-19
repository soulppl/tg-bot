from aiogram.types import CallbackQuery

from modules.keyboards.interests import ikb_menu
from modules.quiz import Quiz
from aiogram.dispatcher import FSMContext
from modules.dp import dp
from constants.message import MESSAGES


@dp.callback_query_handler(state=Quiz.location)
async def keyboard_message(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        location = call.data
        quiz_responses["location"] = location
    await call.message.edit_text(MESSAGES.what_you_are_interesting, parse_mode="HTML")
    await call.message.edit_reply_markup(
        reply_markup=ikb_menu
    )
    await Quiz.next()
