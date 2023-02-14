from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from constants.menu.interests import Interests
from constants.message import MESSAGES
from core.dp import dp
from modules.keyboards.interests import ikb_menu, ikb_menu_with_skip
from modules.quiz import Quiz


@dp.callback_query_handler(state=Quiz.interests, text=Interests.skip)
async def keyboard_message_skip(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        interests = call.data
        quiz_responses["interests"] = interests
    await call.message.edit_text(
        MESSAGES.interests,
        parse_mode="HTML"
    )
    await Quiz.next()


@dp.callback_query_handler(state=Quiz.interests)
async def keyboard_message(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        interests = call.data
        quiz_responses["interests"] = interests
    await call.message.edit_text(
        MESSAGES.interests_with_skip,
        parse_mode="HTML"
    )
    await call.message.edit_reply_markup(
        reply_markup=ikb_menu_with_skip,
    )

