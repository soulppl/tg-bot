from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ForceReply
from constants.message import MESSAGES
from components.about.keyboard import ikb_menu as ikb_menu_about_skip
from constants.quiz_responses import QuizResponses
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state: FSMContext):
    await tell_about_yourself(call.message, state)


async def tell_about_yourself(message: types.Message, state: FSMContext):
    message_answer = await message.answer(
        MESSAGES.tell_about_yourself,
        reply_markup=ikb_menu_about_skip,
        parse_mode="HTML"
    )
    await message.delete()
    async with state.proxy() as globalState:
        globalState[QuizResponses.service_data.last_message] = message_answer

    await Quiz.preview.set()

