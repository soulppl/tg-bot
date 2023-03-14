from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.quiz_responses_fields import QuizResponsesFields


async def delete_message(message: types.Message):
    if message.reply_to_message:
        await message.reply_to_message.delete()
    if message:
        await message.delete()


async def delete_cached_messages(state: FSMContext):
    async with state.proxy() as globalState:
        try:
            cached_message = globalState[QuizResponsesFields.service_data.last_message]
            await delete_message(cached_message)
        except Exception as inst:
            globalState[QuizResponsesFields.service_data.last_message] = None


async def clear_user_history_and_state(state: FSMContext):
    await delete_cached_messages(state)
    await state.finish()
