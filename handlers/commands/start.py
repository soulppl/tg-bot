from aiogram import types
from aiogram.dispatcher import FSMContext
from modules.dp import dp
from utils.say_welcome import say_welcome


async def start(message: types.Message, state: FSMContext):
    await say_welcome(message, state)
