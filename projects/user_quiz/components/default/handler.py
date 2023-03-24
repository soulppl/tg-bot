import os

from aiogram import types

from utils.authorization import handled_auth_user

from utils.clear_user_history import delete_message


async def default(message: types.Message):
    if message.chat.type != 'private':
        return
    await handled_auth_user(message)
    await delete_message(message)
