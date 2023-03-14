from aiogram import types
from utils.authorization import handled_auth_user


async def default(message: types.Message):
    if message.chat.type != 'private':
        return
    await handled_auth_user(message)
