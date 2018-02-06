import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/gzingale/Downloads/SmartthingsEvents-2e63a60cb811.json', scope)
# credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/gzingale/Downloads/ClientSecret.json', scope)

gc = gspread.authorize(credentials)

wks = gc.openall()

print wks 
print len(wks)

logsBooks = gc.open_by_key('1htjOj1B9jdm-eRvV7_52ARj9wjNijTJ3ZPz53-LcqXY')

logsSheet = logsBooks.get_worksheet(0)

val = logsSheet.acell('B3').value

print val
