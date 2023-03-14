from aiogram.types import CallbackQuery, InputMediaPhoto

from components.interests_with_skip.keyboard import ikb_menu
from aiogram.dispatcher import FSMContext
from constants.message import MESSAGES
from constants.quiz_responses_fields import QuizResponsesFields
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as quiz_responses:
        interests = call.data
        if QuizResponsesFields.interests in quiz_responses:
            quiz_responses[QuizResponsesFields.interests] = list(
                dict.fromkeys(quiz_responses[QuizResponsesFields.interests] + [interests])
            )
        else:
            quiz_responses[QuizResponsesFields.interests] = [interests]
    photo = open('./components/interests/interests.jpg', 'rb')

    message_answer = await call.message.answer_photo(
        photo=photo,
        caption=MESSAGES.what_you_are_interesting_with_skip,
        reply_markup=ikb_menu,
        parse_mode="HTML",
    )
    async with state.proxy() as globalState:
        globalState[QuizResponsesFields.service_data.last_message] = message_answer

    await call.message.delete()
