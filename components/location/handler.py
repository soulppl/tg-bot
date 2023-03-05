from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.message import MESSAGES
from components.location.keyboard import ikb_menu
from modules.Quiz import Quiz


async def default(message: types.Message, state: FSMContext):
    async with state.proxy() as quiz_responses:
        name = message.text
        quiz_responses["name"] = name
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await ask_location(message, state)


async def ask_location(message: types.Message, state: FSMContext):
    async with state.proxy() as quiz_responses:
        name = quiz_responses["name"]
        message_answer = await message.answer(
            MESSAGES.where_are_you.substitute(name=name),
            parse_mode='HTML',
            reply_markup=ikb_menu
        )
        quiz_responses["_message"] = message_answer
        await message.delete()
        if "is_editing" in quiz_responses:
            await Quiz.preview.set()
            return
        await Quiz.next()
