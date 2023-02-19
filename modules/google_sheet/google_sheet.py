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

invite_link_idx = 9

range_full_table = "Sheet1!A1:J3000"
range_id = "Sheet1!B1:B3000"
google_table_secret_abs_path = os.path.expanduser(GOOGLE_TABLE_SECRET_FILE_PATH)
credentials = service_account.Credentials.from_service_account_file(google_table_secret_abs_path, scopes=scopes)
service = discovery.build('sheets', 'v4', credentials=credentials)


async def send_user_info_to_sheets(user_info):
    try:
        print(user_info)

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


def is_user_authorised(user_id):
    user_row = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_id
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
