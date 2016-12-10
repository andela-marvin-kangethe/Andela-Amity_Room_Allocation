import sqlite3
from app.storage import Storage
from app.room import Room
from app.person import Person

class Database(Storage):

	def __init__(self):
		self.db_name = None
		self.db = None
		self.cursor = None

	def create_db_to_use(self, db_Name):
		self.db_name = db_Name
		if self.db_name[-2:].upper() != "DB":
			self.db_name += ".db"

		self.openDB()
		self.closeDB()

	def openDB(self):
		self.db = sqlite3.connect(self.db_name)
		self.cursor = self.db.cursor()
	
	def closeDB(self):
		self.cursor.close()
		self.db.close()

	def create_tables_to_use(self):
		self.openDB()
		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS Rooms
				(
				Room_name TEXT NOT NULL UNIQUE,
				ROOM_TYPE TEXT NOT NULL,
				ROOM_MEMEBER_1 TEXT NULL,
				ROOM_MEMEBER_2 TEXT NULL,
				ROOM_MEMEBER_3 TEXT NULL,
				ROOM_MEMEBER_4 TEXT NULL,
				ROOM_MEMEBER_5 TEXT NULL,
				ROOM_MEMEBER_6 TEXT NULL
					)
			''')

		self.db.commit()

		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS Person
				(
				Person_name TEXT NOT NULL ,
				Person_id INT NOT NULL PRIMARY KEY UNIQUE,
				Person_job TEXT NOT NULL,
				Wants_Room TEXT NOT NULL,
				Is_Allocated TEXT NOT NULL
					)
			''')

		self.db.commit()

		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS Room_Members
				(
				Room_Name TEXT NOT NULL,
				Person_id INT NOT NULL
					)
			''')

		self.db.commit()

		self.closeDB()	

	def insert_room_data_into_db(self):
		
		self.openDB()
		try:
			if len(Storage.list_of_all_rooms) > 0:
				for rooms in range(0, len(Storage.list_of_all_rooms)):
					Room_Name = Storage.list_of_all_rooms[rooms].Room_name
					Room_Type = Storage.list_of_all_rooms[rooms].Room_type
					Room_Member = Storage.list_of_all_rooms[rooms].Room_instance.current_members
					for rooms in range(len(Room_Member),6):
						Room_Member.append("")
					self.cursor.execute('''
				        INSERT INTO Rooms VALUES(?,?,?,?,?,?,?,?) ''',(
				        	Room_Name, 
				        	Room_Type,
				        	Room_Member[0],
				        	Room_Member[1],
				        	Room_Member[2],
				        	Room_Member[3],
				        	Room_Member[4],
				        	Room_Member[5]))
					self.db.commit()

					for members in range(len(Room_Member)):
						self.cursor.execute('''
				        	INSERT INTO Room_Members VALUES(?,?) ''',(Room_Name, Room_Member[members]))
						self.db.commit()

		except Exception as e:
			raise e
		self.closeDB()

	def insert_person_data_into_db(self):
		
		self.openDB()
		try:
			if len(Storage.list_of_all_people) > 0:
				for pple in range(0, len(Storage.list_of_all_people)):
					Person_Name = Storage.list_of_all_people[pple].name
					Person_Type = Storage.list_of_all_people[pple].jobType
					Person_id = Storage.list_of_all_people[pple].id_no
					Person_wants_room = Storage.list_of_all_people[pple].wantsRoom
					Person_is_allocated = Storage.list_of_all_people[pple].andelan.is_allocated(Person_id)

					self.cursor.execute('''
				        INSERT INTO Person VALUES(?,?,?,?,?) ''',(
				        	Person_Name, 
				        	Person_id, 
				        	Person_Type, 
				        	Person_wants_room, 
				        	Person_is_allocated)
				        )
					self.db.commit()


		except Exception as e:
			raise e
		self.closeDB()	

	def retieve_data_from_db_for_unallocated(self):
		#Collect data to store in unallocated. { Names }
		# 1 is true and 0 is false.
		self.openDB()
		try:
			self.cursor.execute('''
				SELECT * FROM Person WHERE Wants_Room = ? AND Is_Allocated = ? 
			''',("YES","0"))

			data = self.cursor.fetchall()
			Storage.list_of_unallocated_people = []
			for rows in data:
				Storage.list_of_unallocated_people.append(int(rows[1]))
				Storage.unallocated_people_info[int(rows[1])] = str(rows[0])
		except Exception as e:
			raise e
		self.closeDB()

	def retieve_data_from_db_for_allocated(self):
		#Collect data to store in allocated. { Names }
		self.openDB()
		try:
			self.cursor.execute('''
				SELECT Person_name FROM Person WHERE Wants_Room = ? AND Is_Allocated = ? 
			''',("YES","1"))

			data = self.cursor.fetchall()
			Storage.list_of_allocated_people = []
			for rows in data:
				Storage.list_of_allocated_people.append(str(rows[0]))
		except Exception as e:
			raise e
		self.closeDB()

	def retieve_data_from_db_for_all_rooms(self):
		#Collect data to store in allocated. { Names }

		self.openDB()
		try:
			new_room_name = ""
			new_room_type = ""
			room = None
			self.cursor.execute('''
				SELECT * FROM Rooms 
			''')

			data = self.cursor.fetchall()
			Storage.list_of_all_rooms = []
			for rows in data:
				new_room_name = rows[0]
				new_room_type = rows[1]
				MyList = [rows[2],rows[3],rows[4],rows[5],rows[6],rows[7]]
				
				room = Room(new_room_name, new_room_type)
				for mem in range(len(MyList)):
					if MyList[mem] != "":
						room.Room_instance.current_members.append(str(MyList[mem]))
				
				Storage.list_of_all_rooms.append(room)

			#print "\n",Storage.list_of_allocated_people	
		except Exception as e:
			raise e
		self.closeDB()

	def retieve_data_from_db_for_people_info(self):
		self.openDB()
		try:
			Storage.people_info = {}
			self.cursor.execute('''
				SELECT * FROM Person WHERE Wants_Room = ?
			''',("YES",))
			data = self.cursor.fetchall()
			for rows in data:
				Storage.people_info[rows[1]] = str(rows[0])
		except Exception as e:
			raise e
		self.closeDB()	
	
	def retieve_data_from_db_for_all_people(self):
		self.openDB()
		try:
			self.cursor.execute('''
				SELECT * FROM Person
			''')
			info = self.cursor.fetchall()
			for rows in info:
				pp = Person(rows[0], rows[2], rows[3], 1, rows[1])
				Storage.list_of_all_people.append(pp)

		except Exception as e:
			raise e
		self.closeDB()

	def clear_tables(self):
		pass

	def Save(self,database):
		self.database = database
		self.create_db_to_use(self.database)
		self.create_tables_to_use()
		self.insert_room_data_into_db()
		self.insert_person_data_into_db()

	def Load(self,database):
		self.db_name = "{}.db".format(database)
		self.retieve_data_from_db_for_allocated()
		self.retieve_data_from_db_for_unallocated()
		self.retieve_data_from_db_for_all_rooms()
		self.retieve_data_from_db_for_people_info()	
		self.retieve_data_from_db_for_all_people()	







