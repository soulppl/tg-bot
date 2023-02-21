from aiogram import types

from modules.dp import dp, bot


@dp.message_handler(state="*")
async def chat_handler(message: types.Message):
    print('auf')
    chat = await bot.get_chat(message.chat.id)
    print(chat)
