import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ForceReply, Chat

from constants.message import MESSAGES
from modules.google_sheet.google_sheet import is_user_authorised, restore_invite_link
from modules.quiz import Quiz
from modules.dp import dp
from utils.authorization import handled_auth_user


@dp.message_handler(commands=['start'], state=None)
async def send_message(message: types.Message, state=FSMContext):
    await say_welcome(message, state)


async def say_welcome(message: types.Message, state=FSMContext):
    user_id = message.from_user.id
    user_exists = is_user_authorised(user_id)
    if user_exists:
        await handled_auth_user(message)
        return
    message_answer = await message.answer(
        MESSAGES.your_name,
        reply_markup=ForceReply().create(),
        parse_mode="HTML"
    )
    await message.delete()
    async with state.proxy() as globalState:
        globalState["_message"] = message_answer
    await Quiz.name.set()
