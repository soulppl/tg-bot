from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Chat

from constants.message import MESSAGES
from core.dp import dp
from modules.google_sheet.google_sheet import send_user_info_to_sheets
from modules.quiz import Quiz


@dp.message_handler(state=Quiz.who_am_i)
async def send_message(message: types.Message, state=FSMContext):
    async with state.proxy() as quiz_responses:
        who_am_i = message.text
        quiz_responses["who_am_i"] = who_am_i
    await message.delete()
    await message.reply_to_message.delete()
    # todo: try catch
    chat = Chat.get_current()
    user_url_id = chat.user_url
    user_answers_dict = quiz_responses.values()
    user_answers_list = list(user_answers_dict)
    user_name = message.from_user.username
    user_url_name = f"t.me/{user_name}"
    user_info = [user_name, user_url_name, user_url_id] + user_answers_list
    send_user_info_to_sheets(user_info)
    await message.answer(MESSAGES.who_am_i, parse_mode='HTML')
    await Quiz.next()
