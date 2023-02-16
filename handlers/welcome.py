from aiogram import types
from aiogram.types import ForceReply, Chat

from constants.message import MESSAGES
from modules.quiz import Quiz
from core.dp import dp, bot


@dp.message_handler(commands=['start'], state=None)
async def send_message(message: types.Message):
    await message.answer(MESSAGES.welcome, reply_markup=ForceReply().create())
    # chat = Chat.get_current(False)
    # print(chat)
    # chat.get
    # print(chat.user_url)
    await Quiz.name.set()
