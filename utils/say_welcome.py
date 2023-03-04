from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ForceReply

from constants.message import MESSAGES
from modules.quiz import Quiz
from utils.authorization import handled_auth_user


async def say_welcome(message: types.Message, state: FSMContext):
    user_exists = await handled_auth_user(message)
    if user_exists:
        return

    message_answer = await message.answer(
        MESSAGES.your_name,
        reply_markup=ForceReply().create(),
        parse_mode="HTML"
    )
    await message.delete()
    async with state.proxy() as globalState:
        globalState["_message"] = message_answer
        if "is_editing" in globalState:
            await Quiz.who_am_i.set()
            return
    await Quiz.name.set()
