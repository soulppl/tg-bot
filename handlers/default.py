from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.welcome import say_welcome
from modules.dp import dp
from utils.authorization import handled_auth_user


@dp.message_handler()
async def answer_to_auth_user(message: types.Message):
    print('answer_to_auth_user:')
    print(message.from_user.id)
    if message.chat.type != 'private':
        return
    await handled_auth_user(message)


@dp.message_handler(commands=['restart'], state="*")
async def clear_state(message: types.Message, state=FSMContext):
    if message.chat.type != 'private':
        return

    user_exists = await handled_auth_user(message)
    if not user_exists:
        async with state.proxy() as globalState:
            try:
                cached_message = globalState["_message"]
                if cached_message:
                    await cached_message.delete()
                if cached_message.reply_to_message:
                    cached_message.reply_to_message.delete()
            except Exception as inst:
                globalState["_message"] = None
                print('Error: message not found')

        await state.finish()
        await say_welcome(message, state)
        return
