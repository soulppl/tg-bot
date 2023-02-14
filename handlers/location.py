from aiogram.types import CallbackQuery

from modules.keyboards.interests import ikb_menu
from modules.quiz import Quiz
from aiogram.dispatcher import FSMContext
from core.dp import dp
from constants.message import MESSAGES


# @dp.message_handler(state=Quiz.location)
# async def send_message(message: types.Message, state=FSMContext):
#     async with state.proxy() as quiz_responses:
#         location = message.text
#         quiz_responses["location"] = location
#     await message.answer(f"User location {location}")
#     await Quiz.next()


@dp.callback_query_handler(state=Quiz.location)
async def keyboard_message(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        location = call.data
        quiz_responses["location"] = location
    await call.message.edit_text(f"Super, you are in {location}!\n\n{MESSAGES.location}", parse_mode="HTML")
    await call.message.edit_reply_markup(
        reply_markup=ikb_menu
    )
    await Quiz.next()
