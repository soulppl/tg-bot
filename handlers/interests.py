from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ForceReply
from constants.menu.interests import Interests
from constants.message import MESSAGES
from modules.dp import dp
from modules.keyboards.interests import ikb_menu_with_skip
from modules.keyboards.travels import ikb_menu
from modules.quiz import Quiz


@dp.callback_query_handler(state=Quiz.interests, text=Interests.skip)
async def keyboard_message_with_skip(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        interests = quiz_responses["interests"]
        if Interests.travels in interests:
            quiz_responses["interests"] = ', '.join(interests)
            await call.message.edit_text(MESSAGES.are_you_interesting_on_yacht, parse_mode="HTML")
            await call.message.edit_reply_markup(
                reply_markup=ikb_menu
            )
            await Quiz.travels.set()
        else:
            quiz_responses["interests"] = ', '.join(interests)
            quiz_responses["travels"] = "_"
            await call.message.answer(
                MESSAGES.tell_about_yourself,
                reply_markup=ForceReply().create(),
                parse_mode="HTML"
            )
            await call.message.delete()
            await Quiz.who_am_i.set()


@dp.callback_query_handler(state=Quiz.interests)
async def keyboard_message(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        interests = call.data
        if "interests" in quiz_responses:
            quiz_responses["interests"] = list(dict.fromkeys(quiz_responses["interests"] + [interests]))
        else:
            quiz_responses["interests"] = [interests]
    await call.message.answer(
        MESSAGES.what_you_are_interesting_with_skip,
        reply_markup=ikb_menu_with_skip,
        parse_mode="HTML"
    )
    await call.message.delete()

