from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from constants.menu.quiz_preview import QuizPreview
from constants.message import MESSAGES
from modules.dp import dp
from modules.keyboards.inline import edit_quiz_ikb_menu
from modules.quiz import Quiz
from utils import get_invite_link, send_user_data, clear_user_history


async def quiz_send(call: CallbackQuery, state: FSMContext):
    invite_link = await get_invite_link(state)
    if call.data == QuizPreview.send_quiz:
        print('send')
        print(call.data)
        await call.message.answer(
            MESSAGES.invite_link.substitute(
                invite_link=invite_link
            )
        )
    else:
        print('edit')
        message_answer = await call.message.edit_text(
            MESSAGES.choose_edit_step,
            parse_mode="HTML"
        )
        await call.message.edit_reply_markup(
            reply_markup=edit_quiz_ikb_menu
        )
        async with state.proxy() as globalState:
            globalState["_message"] = message_answer
        await Quiz.quiz_edit.set()
        return

    await send_user_data(state)
    await clear_user_history(state)

    await call.message.delete()
    await state.finish()
