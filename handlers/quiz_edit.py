from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from constants.menu.edit_quiz import EditQuizSteps
from handlers.interests import tell_about_yourself
from handlers.name import ask_location
from utils import say_welcome


async def quiz_edit(call: CallbackQuery, state: FSMContext):
    if call.data == EditQuizSteps.name:
        async with state.proxy() as globalState:
            globalState["is_editing"] = True
            globalState["editing_field"] = "name"
        await say_welcome(call.message, state)
        return
    elif call.data == EditQuizSteps.location:
        async with state.proxy() as globalState:
            globalState["is_editing"] = True
            globalState["editing_field"] = "location"
        await ask_location(call.message, state)
        return
    elif call.data == EditQuizSteps.who_am_i:
        async with state.proxy() as globalState:
            globalState["is_editing"] = True
            globalState["editing_field"] = "who_am_i"
        await tell_about_yourself(call.message, state)
        return

