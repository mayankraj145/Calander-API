# pip install google-api-python-client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()
import pickle
pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
#to get My Calendar events:
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()
result['items'][0]
