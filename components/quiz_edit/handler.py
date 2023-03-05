from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from components.quiz_edit.keyboard import ikb_menu
from constants.message import MESSAGES
from modules.Quiz import Quiz


async def default(call: CallbackQuery, state: FSMContext):

    message_answer = await call.message.edit_text(
        MESSAGES.choose_edit_step,
        parse_mode="HTML"
    )
    await call.message.edit_reply_markup(
        reply_markup=ikb_menu
    )
    async with state.proxy() as globalState:
        globalState["_message"] = message_answer
    await Quiz.editing.set()
    return




# async def default(call: CallbackQuery, state: FSMContext):
#     if call.data == EditQuizSteps.name:
#         async with state.proxy() as globalState:
#             globalState["is_editing"] = True
#             globalState["editing_field"] = "name"
#         await say_welcome(call.message, state)
#         return
#     elif call.data == EditQuizSteps.location:
#         async with state.proxy() as globalState:
#             globalState["is_editing"] = True
#             globalState["editing_field"] = "location"
#         await ask_location(call.message, state)
#         return
#     elif call.data == EditQuizSteps.who_am_i:
#         async with state.proxy() as globalState:
#             globalState["is_editing"] = True
#             globalState["editing_field"] = "who_am_i"
#         await tell_about_yourself(call.message, state)
#         return

