import asyncio
from aiogram import types

from constants.message import MESSAGES
from modules.google_sheet.google_sheet import is_user_authorised, restore_invite_link
from utils.envs import get_rules_info_link, get_auth_user_message_timeout


async def handled_auth_user(message: types.Message):
    user_id = message.from_user.id
    user_exists = is_user_authorised(user_id)
    if user_exists:
        auth_user_message_timeout = get_auth_user_message_timeout()
        invite_link_restored = restore_invite_link(user_id)
        rules_info_link = get_rules_info_link()
        answer = await message.answer(
            MESSAGES.invite_link_restored.substitute(
                invite_link_restored=invite_link_restored,
                rules_info_link=rules_info_link
            )
        )
        await asyncio.sleep(int(auth_user_message_timeout))
        await message.delete()
        await answer.delete()
        return
