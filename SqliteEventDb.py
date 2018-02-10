import sqlite3

class SqliteEventDb(object):

	def __init__(self, db_path):
		self.path = db_path
		self.conn = sqlite3.connect(self.path)


	def save_events(self, event_list):
		c = self.conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS events
             (date datetime, device text not null, event_name text not null, event_value text not null, event_descprition text not null)''')

		for event in event_list:
			c.execute("INSERT INTO events VALUES ('%s','%s','%s','%s','%s')" % (event.time, event.device, event.event_name, event.event_value, event.event_descprition))

		self.conn.commit()
		self.conn.close()
