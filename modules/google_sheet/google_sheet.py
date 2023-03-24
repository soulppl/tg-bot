import os

from apiclient import discovery
from google.oauth2 import service_account
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
GOOGLE_TABLE_SECRET_FILE_PATH = os.getenv("GOOGLE_TABLE_SECRET_FILE_PATH")

scopes = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets"
]

invite_link_idx = 8
referral_idx = 9
last_message_id_idx = 'L'

range_full_table = "Users!A1:K3000"
range_id = "Users!B1:B3000"
range_referrals = "Referrals!A1:C3000"
range_referees = "Users!J1:J3000"
google_table_secret_abs_path = os.path.expanduser(GOOGLE_TABLE_SECRET_FILE_PATH)
credentials = service_account.Credentials.from_service_account_file(google_table_secret_abs_path, scopes=scopes)
service = discovery.build('sheets', 'v4', credentials=credentials)


async def send_user_quiz_to_sheets(user_info):
    try:
        data = {
            'values': [user_info]
        }

        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            body=data,
            range=range_full_table,
            valueInputOption='USER_ENTERED'
        ).execute()

    except OSError as e:
        print(e)


def get_users():
    users = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_full_table,
    ).execute()
    users = users['values'][1:]
    return users


def get_users_ids() -> list[str]:
    users_ids_response = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_id,
        majorDimension='COLUMNS'
    ).execute()
    users_ids = users_ids_response['values'][0][1:]
    return users_ids


def is_user_authorised(user_id):
    user_row = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_id,
    ).execute()
    user_ids_lists = list(user_row.values())[2]
    # лучше не спрашивайте 🧙🪄 вжух
    user_ids_flat_list = [item for sublist in user_ids_lists for item in sublist]

    return f"{user_id}" in user_ids_flat_list


def restore_invite_link(user_id):
    table = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_full_table
    ).execute()
    table_content = list(table.values())[2]
    for row in table_content:
        if f"{user_id}" in row:
            return row[invite_link_idx]


def get_referrals():
    try:
        data = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_referrals,
        ).execute()

        referrals = data['values'][1:]

        return referrals

    except OSError as e:
        print(e)


def get_referrals_referees_list():
    try:
        data = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_referees,
            majorDimension='COLUMNS'
        ).execute()
        referees = data['values'][0][1:]

        return referees

    except OSError as e:
        print(e)


def get_referees():
    try:
        referees_resp = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_referees,
            majorDimension='COLUMNS'
        ).execute()
        referees = referees_resp['values'][0][1:]
        return referees

    except OSError as e:
        print(e)


def set_last_referral_message_id(message_id: list[int], user_idx: str):
    try:
        data = {
            'values': [message_id]
        }

        range_last_message_id = f'Users!{last_message_id_idx}{user_idx}:{last_message_id_idx}{user_idx}'

        service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            body=data,
            range=range_last_message_id,
            valueInputOption='USER_ENTERED'
        ).execute()

    except OSError as e:
        print(e)
