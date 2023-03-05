from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ForceReply
from constants.message import MESSAGES
from modules.DP import dp
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state=FSMContext):
    async with state.proxy() as quiz_responses:
        travels = call.data
        quiz_responses["travels"] = travels
    await call.message.answer(
        MESSAGES.tell_about_yourself,
        reply_markup=ForceReply().create(),
        parse_mode="HTML"
    )
    await call.message.delete()
    await Quiz.preview.set()
