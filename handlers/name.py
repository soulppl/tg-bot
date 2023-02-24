from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.message import MESSAGES
from modules.keyboards.inline.location import ikb_menu
from modules.quiz import Quiz
from modules.dp import dp


async def send_message(message: types.Message, state: FSMContext):
    async with state.proxy() as quiz_responses:
        name = message.text
        quiz_responses["name"] = name
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await ask_location(message, state)


# переиспользуемая функция
async def ask_location(message: types.Message, state: FSMContext):
    print('ask location call')

    async with state.proxy() as quiz_responses:
        name = quiz_responses["name"]
        message_answer = await message.answer(
            MESSAGES.where_are_you.substitute(name=name),
            parse_mode='HTML',
            reply_markup=ikb_menu
        )
        quiz_responses["_message"] = message_answer
        await message.delete()
        if "is_editing" in quiz_responses:
            print('is editing')
            await Quiz.who_am_i.set()
            return
        print('not editing')
        await Quiz.next()
