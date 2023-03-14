from aiogram.types import CallbackQuery, InputMediaPhoto

from components.interests_with_skip.keyboard import ikb_menu
from aiogram.dispatcher import FSMContext
from constants.message import MESSAGES
from constants.quiz_responses import QuizResponses
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as quiz_responses:
        interests = call.data
        if QuizResponses.interests in quiz_responses:
            quiz_responses[QuizResponses.interests] = list(
                dict.fromkeys(quiz_responses[QuizResponses.interests] + [interests])
            )
        else:
            quiz_responses[QuizResponses.interests] = [interests]

    message_answer = await call.message.answer_photo(
        photo='https://drive.google.com/file/d/1GJQFFyStPpyswZ8IMP9zeEIIMY9mYdBI/view?usp=sharing',
        caption=MESSAGES.what_you_are_interesting_with_skip,
        reply_markup=ikb_menu,
        parse_mode="HTML",
    )
    async with state.proxy() as globalState:
        globalState[QuizResponses.service_data.last_message] = message_answer

    await call.message.delete()
