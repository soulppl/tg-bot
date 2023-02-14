from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.message import MESSAGES
from core.dp import dp
from modules.quiz import Quiz


@dp.message_handler(state=Quiz.who_am_i)
async def send_message(message: types.Message, state=FSMContext):
    async with state.proxy() as quiz_responses:
        who_am_i = message.text
        quiz_responses["who_am_i"] = who_am_i
    await message.answer(MESSAGES.who_am_i, parse_mode='HTML')
    await Quiz.next()
