import os

from aiogram import types

from utils.authorization import handled_auth_user

from utils.clear_user_history import delete_message

API_TOKEN = os.getenv("BOT_API_TOKEN")
api_id = 6275419559
api_hash = 'AAEIsSMXFIedarHGPS673SgEEFwnOEvWVe8'


async def default(message: types.Message):
    if message.chat.type != 'private':
        return
    await handled_auth_user(message)
    await delete_message(message)
