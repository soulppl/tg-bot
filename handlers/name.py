from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.message import MESSAGES
from modules.keyboards.location import ikb_menu
from modules.quiz import Quiz
from modules.dp import dp


@dp.message_handler(state=Quiz.name)
async def send_message(message: types.Message, state=FSMContext):
    async with state.proxy() as quiz_responses:
        name = message.text
        quiz_responses["name"] = name
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await message.answer(
        MESSAGES.where_are_you.substitute(name=name),
        parse_mode='HTML',
        reply_markup=ikb_menu
    )
    await message.delete()

    await Quiz.next()

