from aiogram.types import CallbackQuery

from components.interests_with_skip.keyboard import ikb_menu
from aiogram.dispatcher import FSMContext
from constants.message import MESSAGES


async def default(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as quiz_responses:
        interests = call.data
        if "interests" in quiz_responses:
            quiz_responses["interests"] = list(dict.fromkeys(quiz_responses["interests"] + [interests]))
        else:
            quiz_responses["interests"] = [interests]
    message_answer = await call.message.answer(
        MESSAGES.what_you_are_interesting_with_skip,
        reply_markup=ikb_menu,
        parse_mode="HTML"
    )
    async with state.proxy() as globalState:
        globalState["_message"] = message_answer

    await call.message.delete()
