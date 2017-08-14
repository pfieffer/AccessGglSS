import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import datetime

scope = ['https://spreadsheets.google.com/feeds']
jsonFile = 'Todo.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(jsonFile , scope)
client = gspread.authorize(creds)

gglspreadsheet = 'To-do list'
sheet = client.open(gglspreadsheet).sheet1

pp = pprint.PrettyPrinter()
todos = sheet.get_all_records()
#pp.pprint(todos) 

#print(sheet.row_count) #get row count

#result = sheet.row_values(7) #get 7th row
#result = sheet.col_values(3) #get 3rd column
#pp.pprint(result)

#sheet.update_cell(7, 1, '8/14') #update 7th row, 1st column value to put 'x'


#Inserting row
# day = str(datetime.datetime.now().day)
# month = str(datetime.datetime.now().month)
# today = month+"/"+day;
# new_todo = "Get some life"
# row=["", today, new_todo]
# index = 8
# sheet.insert_row(row, index)


