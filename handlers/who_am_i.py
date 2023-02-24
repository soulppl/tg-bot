
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from constants.message import MESSAGES
from modules.dp import dp
from modules.keyboards.inline.quiz_preview import ikb_menu
from modules.quiz import Quiz
from utils.user_info import get_welcome_topic_text


async def message_handler(message: types.Message, state: FSMContext):
    await send_message(message, message.text, state)


async def callback_handler(call: CallbackQuery, state: FSMContext):
    await send_message(call.message, call.data, state)


async def send_message(message: types.Message, message_text: str, state: FSMContext):
    async with state.proxy() as quiz_responses:
        if "is_editing" in quiz_responses:
            print('messge')
            edited_text = message_text
            edited_field = quiz_responses["editing_field"]
            quiz_responses[edited_field] = edited_text
        else:
            print('who am i')
            who_am_i = message_text
            quiz_responses["who_am_i"] = who_am_i
        welcome_topic_text = get_welcome_topic_text(quiz_responses)
        welcome_preview_text = MESSAGES.welcome_topic_text_preview.substitute(welcome_topic_text=welcome_topic_text)

    message_answer = await message.answer(
        text=welcome_preview_text,
        reply_markup=ikb_menu,
        parse_mode="HTML"
    )

    async with state.proxy() as globalState:
        globalState["_message"] = message_answer

    await message.delete()
    if message.reply_to_message:
        await message.reply_to_message.delete()
    print('set send quiz')
    await Quiz.send_quiz.set()
