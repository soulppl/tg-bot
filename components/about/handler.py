from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ForceReply
from components.interests.keyboard_text import KeyboardText
from constants.message import MESSAGES
from components.travels.keyboard import ikb_menu
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as quiz_responses:
        interests = quiz_responses["interests"]
        if KeyboardText.travels in interests:
            quiz_responses["interests"] = ', '.join(interests)
            message_answer = await call.message.edit_text(MESSAGES.are_you_interesting_on_yacht, parse_mode="HTML")
            await call.message.edit_reply_markup(
                reply_markup=ikb_menu
            )
            quiz_responses["_message"] = message_answer
            await Quiz.travels.set()
            return
        else:
            quiz_responses["interests"] = ', '.join(interests)
            quiz_responses["travels"] = "_"
    await tell_about_yourself(call.message, state)


async def tell_about_yourself(message: types.Message, state: FSMContext):
    message_answer = await message.answer(
        MESSAGES.tell_about_yourself,
        reply_markup=ForceReply().create(),
        parse_mode="HTML"
    )
    await message.delete()
    async with state.proxy() as globalState:
        globalState["_message"] = message_answer

    await Quiz.preview.set()

