from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.message import MESSAGES
from modules.keyboards.location import ikb_menu
from modules.quiz import Quiz
from core.dp import dp


@dp.message_handler(state=Quiz.name)
async def send_message(message: types.Message, state=FSMContext):
    async with state.proxy() as quiz_responses:
        name = message.text
        quiz_responses["name"] = name
    await message.answer(
        MESSAGES.name.substitute(name=name),
        parse_mode='HTML',
        reply_markup=ikb_menu
    )
    await Quiz.next()

