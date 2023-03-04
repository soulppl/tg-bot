from aiogram import types
from utils.authorization import handled_auth_user


async def answer_to_auth_user(message: types.Message):
    print('answer_to_auth_user:')
    print(message.from_user.id)
    if message.chat.type != 'private':
        print('auth')
        return
    print('not auth')
    await handled_auth_user(message)
