import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Todo.json', scope)
client = gspread.authorize(creds)

sheet = client.open('To-do list').sheet1

todos = sheet.get_all_records()
print(todos)
