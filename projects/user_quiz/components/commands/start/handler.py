from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.say_welcome import say_welcome


async def default(message: types.Message, state: FSMContext):
    await say_welcome(message, state)
