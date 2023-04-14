from aiogram import types

from modules.google_sheet import google_sheet
from projects.chat_member.components.unsubscrive.constants import ChatMemberStatus


async def default(chat_member: types.ChatMemberUpdated):
    if chat_member.new_chat_member.status == ChatMemberStatus.left:
        delete_user(chat_member.from_user)


def delete_user(user: types.User):
    print('delete user')
    print(user)
    users_ids = google_sheet.get_users_ids()
    user_idx = users_ids.index(f'{user.id}')
    user_idx_with_shift = user_idx + google_sheet.gsheet_shift
    google_sheet.delete_user(user_idx_with_shift)
