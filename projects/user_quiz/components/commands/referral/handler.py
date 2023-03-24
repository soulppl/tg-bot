import asyncio

import typing

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Chat
from aiogram.utils.deep_linking import get_start_link

from constants.message import MESSAGES
from modules.Quiz import Quiz
from projects.user_quiz.components.commands.referral.keyboard import ikb_menu, ikb_menu_referral_list
from utils import get_auth_user_message_timeout
from utils.authorization import is_user_exists
from utils.clear_user_history import delete_message
from utils.referral import is_user_in_referral_list, get_referral_list, ger_referral_number, set_last_message_id


async def default(message: typing.Union[types.Message, types.CallbackQuery], state: FSMContext):
    if isinstance(message, types.Message):
        message = message
    else:
        message = message.message

    is_referral = is_user_in_referral_list(message)
    is_exists = is_user_exists(message)
    if not is_referral or not is_exists:
        await answer_unauthorized(message, state)
        return

    await answer(message, state)


async def answer(message: types.Message, state: FSMContext):
    referral_link = await get_start_link(message.chat.username)
    referral_number = ger_referral_number(message, state)

    message_answer = await message.answer(
        MESSAGES.referral_menu.substitute(
            referral_link=referral_link,
            referees_number=referral_number,
        ),
        reply_markup=ikb_menu,
        parse_mode='HTML'
    )

    set_last_message_id(message_answer, state)

    await delete_message(message)

    await Quiz.referral.set()


async def answer_unauthorized(message: types.Message, state: FSMContext):
    auth_user_message_timeout = get_auth_user_message_timeout()

    message_answer = await message.answer(
        MESSAGES.referral_unauthorized,
        parse_mode='HTML'
    )

    await delete_message(message)
    await asyncio.sleep(int(auth_user_message_timeout))
    await delete_message(message_answer)


async def close(call: types.CallbackQuery, state: FSMContext):
    await delete_message(call.message)
    await state.finish()

    return


async def show_referral_list(call: types.CallbackQuery, state: FSMContext):
    referral_list = get_referral_list(call.message, state)
    referral_number = len(referral_list)

    name_idx = 0
    link_idx = 1

    referrals_list_text_with_link = '\n'.join([MESSAGES.referral_user.substitute(
        link=referral[link_idx],
        name=referral[name_idx],
    ) for referral in referral_list])

    message_answer = await call.message.edit_text(
        text=MESSAGES.referral_user_list.substitute(
            referees_number=referral_number,
            referrals_list=referrals_list_text_with_link,
        ),
        reply_markup=ikb_menu_referral_list,
        disable_web_page_preview=True,
        parse_mode='HTML'
    )
    return
