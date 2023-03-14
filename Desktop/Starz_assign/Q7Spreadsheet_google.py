import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up credentials and authorize access to Google Sheets API
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/spreadsheets'])
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Set up the Google Sheets API client
service = build('sheets', 'v4', credentials=creds)

# Set up the push notification channel
spreadsheet_id = '<YOUR_SPREADSHEET_ID>'
sheet_range = '<YOUR_SHEET_RANGE>'
channel_id = '<YOUR_CHANNEL_ID>'
push_notifications = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[sheet_range], includeGridData=False).execute()
sheet_id = push_notifications['sheets'][0]['properties']['sheetId']
requests = [
    {
        'addSheet': {
            'properties': {
                'title': 'Push Notification Channel',
                'sheetType': 'GRID',
                'gridProperties': {
                    'rowCount': 1,
                    'columnCount': 1,
                    'frozenRowCount': 1
                }
            }
        }
    },
    {
        'updateSheetProperties': {
            'properties': {
                'sheetId': sheet_id,
                'gridProperties': {
                    'rowCount': push_notifications['sheets'][0]['properties']['gridProperties']['rowCount'] + 1
                }
            },
            'fields': 'gridProperties.rowCount'
        }
    }
]
push_notifications = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body={'requests': requests}).execute()
channel_url = push_notifications['replies'][0]['addSheet']['data']['basicFilter']['criteria']['hiddenValues'][0]
channel_id = channel_url[channel_url.rindex('/') + 1:]


def on_message(message):
    global service, sheet_id, channel_id
    if message['resourceId']['kind'] == 'spreadsheet#sheet' and message['resourceId']['sheetId'] == sheet_id and message['channelId'] == channel_id:
        # A change notification was received for the monitored sheet
        try:
            values = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()
        except HttpError as error:
            print(f'Error retrieving updated data: {error}')
            return
        updated_data = values['values']
       

push_notifications = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[sheet_range], includeGridData=False).execute()
channel = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=['Push Notification Channel'], includeGridData=False).execute()
channel_url = channel['sheets'][0]['basicFilter']['criteria']['hiddenValues'][0]
channel_id = channel_url[channel_url.rindex('/')]




