from aiogram import types
from constants.message import MESSAGES
from modules.quiz import Quiz
from core.dp import dp


@dp.message_handler(commands=['start'], state=None)
async def send_message(message: types.Message):
    await message.answer(MESSAGES.welcome)
    await Quiz.name.set()
