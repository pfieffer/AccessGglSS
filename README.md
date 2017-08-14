# Access Google Spreadsheet from terminal

> Uses gspread and oauth2client libraries

Setup:

1. Clone the repo.
2. Open `https://console.developers.google.com/apis` on your browser and create a project.
3. On the Dashboard, add google drive api to your project
4. Go to "Credentials" and put "Web Server" on the "Where you will be accessing the api from?"
5. Give access to "Application data" and "No I'm not using them"
6. Click on "What credentials do I need?"
7. Create a service account giving it a name and give it a role of "Editor"
8. Click "Continue" which will download a json file, rename it to anything you want and move it to the directory where you cloned the repo.
9. Open the json file and copy the `client_email`.
10. Create a google spreadsheet at `https://docs.google.com/spreadsheets` (Skip this if you already have a google spreadsheet)
11. On your spreadsheet, share it to the `client_email`
12. Open spreadsheet.py and change `gglspreadsheet = 'To-do list'` to `gglspreadsheet = 'your_google_spreadsheet_name'` and change `jsonFile = 'Todo.json'` to `jsonFile = 'name_of_json_file_you_downloaded.json'`
13. Open terminal and run `python spreadsheet.py`



