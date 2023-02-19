from aiogram import types

from modules.dp import dp
from modules.google_sheet.google_sheet import is_user_authorised
from utils.authorization import handled_auth_user


@dp.message_handler()
async def answer_to_auth_user(message: types.Message):
    if message.chat.type != 'private':
        return
    await handled_auth_user(message)
