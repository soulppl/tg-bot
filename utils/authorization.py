import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.message import MESSAGES
from constants.quiz_responses_fields import QuizResponsesFields
from modules.DP import bot
from modules.google_sheet.google_sheet import is_user_authorised, restore_invite_link
from utils.envs import get_rules_info_link, get_auth_user_message_timeout, get_forum_id


async def handled_auth_user(message: types.Message):
    user_id = message.from_user.id
    user_exists = is_user_authorised(user_id)
    if user_exists:
        auth_user_message_timeout = get_auth_user_message_timeout()
        invite_link_restored = restore_invite_link(user_id)
        answer = await message.answer(
            MESSAGES.invite_link_restored.substitute(
                invite_link_restored=invite_link_restored
            )
        )
        await asyncio.sleep(int(auth_user_message_timeout))
        await message.delete()
        await answer.delete()
        return True
    return False


async def get_invite_link(state: FSMContext):
    forum_id = get_forum_id()
    async with state.proxy() as quiz_responses:
        if QuizResponsesFields.invite_link not in quiz_responses:
            invite_link_obj = await bot.create_chat_invite_link(
                chat_id=forum_id,
                member_limit=1
            )
            quiz_responses[QuizResponsesFields.invite_link] = invite_link_obj.invite_link

    return quiz_responses[QuizResponsesFields.invite_link]

