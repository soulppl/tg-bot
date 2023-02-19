import asyncio

from aiogram import types
from aiogram.types import ForceReply, Chat

from constants.message import MESSAGES
from modules.google_sheet.google_sheet import is_user_authorised, restore_invite_link
from modules.quiz import Quiz
from modules.dp import dp
from utils.authorization import handled_auth_user
from utils.user_info import get_welcome_topic_text


@dp.message_handler(commands=['start'], state=None)
async def send_message(message: types.Message):
    user_id = message.from_user.id
    user_exists = is_user_authorised(user_id)
    if user_exists:
        await handled_auth_user(message)
        return
    await message.answer(MESSAGES.your_name, reply_markup=ForceReply().create(), parse_mode="HTML")
    await message.delete()

    await Quiz.name.set()
