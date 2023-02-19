import asyncio
from aiogram import types

from constants.message import MESSAGES
from modules.google_sheet.google_sheet import is_user_authorised, restore_invite_link


async def handled_auth_user(message: types.Message):
    user_id = message.from_user.id
    user_exists = is_user_authorised(user_id)
    if user_exists:
        invite_link_restored = restore_invite_link(user_id)
        answer = await message.answer(
            MESSAGES.invite_link_restored.substitute(
                invite_link_restored=invite_link_restored
            )
        )
        await asyncio.sleep(2)
        await message.delete()
        await answer.delete()
        return
