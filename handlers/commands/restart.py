from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import clear_user_history, say_welcome


async def restart(message: types.Message, state: FSMContext):
    if message.chat.type != 'private':
        return

    await clear_user_history(state)
    await say_welcome(message, state)
