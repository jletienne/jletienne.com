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



# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.
OAUTH2_SCOPE = ['https://www.googleapis.com/auth/drive']
# Location of the client secrets.
CLIENT_SECRETS = 'client_secrets.json'


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


# convenience routines
def find_sheet_id_by_name(sheet_name):
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


def get_final_sheet_row_number():
    sheet = API.spreadsheets()
    result = sheet.values().get(spreadsheetId = '1fSf8fvu9hfxtU1DTTfyokIU1SIvzy26dmEVaamIdzTU', range='song_data!A:A').execute()
    values = result.get('values', [])

    return len(values)


def push_csv_to_gsheet(csv_path, sheet_id, start_row):
    #with open(csv_path, 'r') as csv_file:
    csvContents = csv_path.read()

    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": start_row,  # adapt this if you need different positioning
                    "columnIndex": "0", # adapt this if you need different positioning
                },
                "data": csvContents,
                "type": 'PASTE_NORMAL',
                "delimiter": ',',
            }
        }]
    }
    request = API.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body)
    response = request.execute()
    return response



SPREADSHEET_ID = '1fSf8fvu9hfxtU1DTTfyokIU1SIvzy26dmEVaamIdzTU' # Get this one from the link in browser
worksheet_name = 'song_data'
#path_to_csv = 'final2.csv' # change this to a csv stream

def do_all(path_to_csv):
    push_csv_to_gsheet(
        csv_path=path_to_csv,
        sheet_id=find_sheet_id_by_name(worksheet_name),
        start_row=get_final_sheet_row_number()
    )

    return 'yes'

def do_all2(path_to_csv):
    push_csv_to_gsheet(
        csv_path=path_to_csv,
        sheet_id=find_sheet_id_by_name('max_date_uts'),
        start_row=0
    )

    return 'max_date_uts updated success!'

def get_last_date():

    sheet = API.spreadsheets()
    result = sheet.values().get(spreadsheetId = '1fSf8fvu9hfxtU1DTTfyokIU1SIvzy26dmEVaamIdzTU', range='max_date_uts!A2').execute()
    values = result.get('values', [])

    return int(values[0][0])



if __name__ == '__main__':
    print(get_last_date())
    #main()

    print('done')
