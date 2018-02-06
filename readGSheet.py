import gspread
from oauth2client.service_account import ServiceAccountCredentials



class Event(object):

	def __init__(self, time, device, event_name, event_value, event_descprition):
		self.time = time
		self.device = device
		self.event_name = event_name
		self.event_value = event_value
		self.event_descprition = event_descprition

def get_all_events(logBook):
	logsSheet = logsBook.get_worksheet(0)

# 	val = logsSheet.acell('B3').value

# print val


	events = []

	for row in logsSheet.get_all_values():
		# print row
		if row[0] == 'Date/Time':
			#this is the first row ignore it
			continue

		# print row[0]
		# print row[1]
		# print row[2]
		# print row[3]
		# print row[4]
		events.append(Event(row[0],row[1], row[2], row[3], row[4]))

	return events



def log_in(creds_path):

	scope = ['https://spreadsheets.google.com/feeds']

	credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
	# credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/gzingale/Downloads/ClientSecret.json', scope)

	gc = gspread.authorize(credentials)

	return gc

# wks = gc.openall()

# print wks 
# print len(wks)

path = '/Users/gzingale/Downloads/SmartthingsEvents-2e63a60cb811.json'

gc = log_in(path)

logsBook = gc.open_by_key('1htjOj1B9jdm-eRvV7_52ARj9wjNijTJ3ZPz53-LcqXY')

events = get_all_events(logsBook)

print events[0].time

print len(events)


