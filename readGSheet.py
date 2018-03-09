import gspread
from oauth2client.service_account import ServiceAccountCredentials
from SqliteEventDb import *



class Event(object):

	def __init__(self, time, device, event_name, event_value, event_descprition):
		self.time = time
		self.device = device
		self.event_name = event_name
		self.event_value = event_value
		self.event_descprition = event_descprition

def get_all_events(logsSheet):

	events = []

	for row in logsSheet.get_all_values():
		# print row
		if row[0] == 'Date/Time':
			#this is the first row ignore it
			continue

		if row[0] == "" or row[0] is None:
			# We don't want to save empty rows
			continue

		events.append(Event(row[0],row[1], row[2], row[3], row[4]))

	return events



def log_in(creds_path):

	scope = ['https://spreadsheets.google.com/feeds']

	credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)

	gc = gspread.authorize(credentials)

	return gc

def save_events_to_db(event_list):
	db = SqliteEventDb("../events.db")
	db.save_events(event_list)


def delete_saved_events(worksheet, number_events_saved):
	for i in range(number_events_saved):
		worksheet.delete_row(2)

path = '../SmartthingsEvents-2e63a60cb811.json'

gc = log_in(path)

logsBook = gc.open_by_key('1htjOj1B9jdm-eRvV7_52ARj9wjNijTJ3ZPz53-LcqXY')

logsSheet = logsBook.get_worksheet(0)

events = get_all_events(logsSheet)

print(len(events), " were downloaded")

save_events_to_db(events)

print(len(events), " were saved")

delete_saved_events(logsSheet, len(events))

print(len(events), " were deleted")

print(events[0].time)

print(len(events))

