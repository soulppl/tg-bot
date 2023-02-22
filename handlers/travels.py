from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ForceReply
from constants.message import MESSAGES
from modules.dp import dp
from modules.quiz import Quiz


@dp.callback_query_handler(state=Quiz.travels)
async def keyboard_message(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        travels = call.data
        quiz_responses["travels"] = travels
    await call.message.answer(
        MESSAGES.tell_about_yourself,
        reply_markup=ForceReply().create(),
        parse_mode="HTML"
    )
    await call.message.delete()
    await Quiz.who_am_i.set()
