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

range_name = "Sheet1!A1:I1000"
google_table_secret_abs_path = os.path.expanduser(GOOGLE_TABLE_SECRET_FILE_PATH)
credentials = service_account.Credentials.from_service_account_file(google_table_secret_abs_path, scopes=scopes)
service = discovery.build('sheets', 'v4', credentials=credentials)


def send_user_info_to_sheets(user_info):
    try:
        print("gogole")
        print(user_info)

        data = {
            'values': [user_info]
        }

        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            body=data,
            range=range_name,
            valueInputOption='USER_ENTERED'
        ).execute()

    except OSError as e:
        print(e)
