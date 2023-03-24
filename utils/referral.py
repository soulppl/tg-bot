from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from modules.google_sheet import google_sheet
from utils.user import get_user_idx


def get_referral(message: Message):
    args = message.get_args()
    return args


def is_user_in_referral_list(message: Message):
    referrals = google_sheet.get_referrals()
    referrals_flat_list = [item for sublist in referrals for item in sublist]
    username = message.chat.username
    return username in referrals_flat_list


def get_referees_idxes(message: Message):
    referee_username = message.chat.username
    referees = google_sheet.get_referees()
    referee_idxes = [index for (index, item) in enumerate(referees) if item == referee_username]
    return referee_idxes


def ger_referral_number(message: types.Message, state: FSMContext):
    referrals = google_sheet.get_referrals_referees_list()
    referrals_number = referrals.count(message.from_user.username)
    return referrals_number


def get_referral_list(message: types.Message, state: FSMContext):
    referee_idxes = get_referees_idxes(message)
    users = google_sheet.get_users()

    username_idx = 0
    name_idx = 4
    username_link_idx = 2
    id_link_idx = 3

    referral_list = []

    for idx in referee_idxes:
        user = users[idx]
        if user[username_idx]:
            referral_list.append([user[username_idx], user[username_link_idx]])
        else:
            referral_list.append([user[name_idx], user[id_link_idx]])

    return referral_list


def set_last_message_id(message: types.Message, state: FSMContext):
    gsheet_shift = 2
    user_idx = get_user_idx(message.chat.id)
    user_real_idx = user_idx + gsheet_shift
    google_sheet.set_last_referral_message_id([message.message_id], user_real_idx)
