#!/usr/bin/python

"""Google Drive Quickstart in Python.
This script uploads a single file to Google Drive.
"""

from __future__ import print_function
import pprint
import httplib2
from googleapiclient.discovery import build
import googleapiclient.http
#from oauth2client.file import Storage

from google.oauth2 import service_account
import base64
import json
import os
import pandas as pd
import io


# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.
OAUTH2_SCOPE = ["https://www.googleapis.com/auth/spreadsheets", 'https://www.googleapis.com/auth/drive']
# Location of the client secrets.
CLIENT_SECRETS = 'client_secrets.json'

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


# Perform OAuth2.0 authorization flow.
# Create an authorized Drive API client.

if os.environ.get('HEROKU'):
    a2 = os.environ.get('GOOGLE_SCROBBLE')
    service_account_info = json.loads(base64.urlsafe_b64decode(a2))
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info)
else:
    credentials = service_account.Credentials.from_service_account_file(
            filename='credentials/scrobble-data-b595e50324ff.json', scopes=OAUTH2_SCOPE)



http = httplib2.Http()
#credentials.authorize(http)
API = build('sheets', 'v4', credentials=credentials)
service = build("drive", "v3", credentials=credentials)


def get_health_steps_df(folder_id):
    all_steps = []

    results = service.files().list(
        q=f"'{folder_id}' in parents and mimeType='text/csv'",
        fields="files(id, name)"
    ).execute()

    files = results.get("files", [])

    for file in files:
        file_id = file["id"]
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = googleapiclient.http.MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)
        df = pd.read_csv(fh)
        all_steps.append(df)

    final_df = pd.concat(all_steps, ignore_index=True)
    #final_df['date_uts'] = final_df['date_uts'].astype(int)
    return final_df


def get_health_weight_df(folder_id):
    all_steps = []

    results = service.files().list(
        q=f"'{folder_id}' in parents and mimeType='text/csv'",
        fields="files(id, name)"
    ).execute()

    files = results.get("files", [])

    for file in files:
        file_id = file["id"]
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = googleapiclient.http.MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)
        df = pd.read_csv(fh)
        if 'Weight (lb)' in df.columns:
            all_steps.append(df)

    final_df = pd.concat(all_steps, ignore_index=True)
    final_df = final_df[['Date/Time', 'Weight (lb)']]
    final_df = final_df.dropna(subset=['Weight (lb)'])
    return final_df

def find_sheet_id_by_name(sheet_name, SPREADSHEET_ID):
    # ugly, but works
    sheets_with_properties = API \
        .spreadsheets() \
        .get(spreadsheetId=SPREADSHEET_ID, fields='sheets.properties') \
        .execute() \
        .get('sheets')

    for sheet in sheets_with_properties:
        if 'title' in sheet['properties'].keys():
            if sheet['properties']['title'] == sheet_name:
                return sheet['properties']['sheetId']

def push_health_to_gsheet(csv_path, sheet_id, SPREADSHEET_ID):
    #with open(csv_path, 'r') as csv_file:
    csvContents = csv_path.read()

    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": 1,  # 1 keeps the header
                    "columnIndex": 0 # adapt this if you need different positioning
                },
                "data": csvContents,
                "type": 'PASTE_NORMAL',
                "delimiter": ','
            }
        }]
    }
    request = API.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body)
    response = request.execute()
    return response


def do_all_health(path_to_csv, SPREADSHEET_ID):

    # Get this one from the link in browser
    worksheet_name = 'Sheet1'

    push_health_to_gsheet(
    csv_path=path_to_csv,
    sheet_id=find_sheet_id_by_name(worksheet_name, SPREADSHEET_ID),
    SPREADSHEET_ID=SPREADSHEET_ID
    )


    return 'yes'


if __name__ == '__main__':
    print(update_google_sheet_health_steps())
