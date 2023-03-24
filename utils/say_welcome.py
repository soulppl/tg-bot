from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ForceReply

from constants.message import MESSAGES
from constants.quiz_responses_fields import QuizResponsesFields
from modules.Quiz import Quiz
from utils.authorization import handled_auth_user
from utils.clear_user_history import delete_message, delete_cached_messages
from utils.referral import get_referral


async def say_welcome(message: types.Message, state: FSMContext):
    user_exists = await handled_auth_user(message)
    if user_exists:
        return

    referral = get_referral(message)

    photo = open('./projects/user_quiz/components/commands/start/name.jpg', 'rb')

    message_answer = await message.answer_photo(
        photo=photo,
        caption=MESSAGES.your_name,
        reply_markup=ForceReply().create(),
        parse_mode="HTML"
    )

    await delete_message(message)
    await delete_cached_messages(state)

    async with state.proxy() as globalState:
        globalState[QuizResponsesFields.referral.referral_nickname] = referral
        globalState[QuizResponsesFields.service_data.last_message] = message_answer
        if QuizResponsesFields.service_data.is_editing in globalState:
            await Quiz.preview.set()
            return
    await Quiz.location.set()
