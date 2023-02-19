from aiogram import types

from modules.dp import dp
from modules.google_sheet.google_sheet import is_user_authorised
from utils.authorization import handled_auth_user


@dp.message_handler()
async def answer_to_auth_user(message: types.Message):
    if message.chat.type != 'private':
        return
    user_id = message.from_user.id
    user_exists = is_user_authorised(user_id)
    if user_exists:
        await handled_auth_user(message)
