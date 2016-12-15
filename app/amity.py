from app.room import Room
from app.person import Person
from app.storage import Storage
from app.db import Database
import random
import os

class Amity(Storage):
	"""docstring for Amity"""		

	def __init__(self):
		#To check for the number random room allocator can be called.
		self.incrementor = 0
		self.db = Database()							
	
	"""
	Create rooms
	Check same names are not used.{ UPPERCASE all room names. }
	Do incrementation on Total_no_of_rooms {Done in room class. }
	"""
	def createRoom(self,room_name = "", room_type = ""):
		self.room_name = room_name.upper()
		if room_type.upper() == "O":
			self.room_type = "OFFICE"
		elif room_type.upper() == "L":
			self.room_type = "LIVINGSPACE"
		else:
			self.room_type = room_type.upper()

		result = False
		Result = ""

		for rooms in range(len(Storage.list_of_all_rooms)):
			if self.room_name == Storage.list_of_all_rooms[rooms].room_name:
				#Check that the room already exist.
				result = True

		if  self.room_name != "" and result != True :#:
			#Create instance of room class
			#room_type = random.choice(["OFFICE","LIVINGSPACE"])
			self.room = Room(self.room_name, self.room_type)

			#Save instance of room in list of all rooms

			Storage.list_of_all_rooms.append(self.room)	

			value = "\t{}\t\t[ {} ]\tcreated successfully!!".format(self.room.room_name, self.room.room_type)
			Result =  "Room created successfully!!"
		else:
			value =  "Room called {} failed to create.".format(self.room_name)
		print value	
		return Result	

	"""
	Allocate person a room
	call the randomRoomAllocator if and only if :
		1.jobtype is fellow or staff 
	{ any case. correct spelling }
		2.the fellow wants room allocation.
	{ for the staff, wantsRoom is ALWAYS YES. }

	"""
	def allocateRoom(self,name = "",jobType = "",wantsRoom="NO"):
		self.name = name

		self.jobType = jobType.upper()
		#Check that wants room is only yes or no
		if not wantsRoom.upper() in ["Y","YE","YES","N","NO"]:
			print "Use 'yes' if you want room allocation, else use 'no'."
			return None
		elif len(Storage.list_of_all_rooms) < 1:
			print "No existing rooms to allocate you for now."
			return None	
		else:
			#Set the wantsRoom variable so that staff cannot decline room allocation.
			if self.jobType == "STAFF":
				self.wantsRoom = "YES"
			else:
				self.wantsRoom = wantsRoom

			"""
			Create the person instance and allocate room 
			if there are available rooms hence save the person in unallocated list.
			"""  
			if self.wantsRoom.upper() in ["Y","YE","YES"]:
				self.wantsRoom = "YES"
				self.person = Person(self.name,self.jobType,self.wantsRoom,0,0)
				Storage.list_of_all_people.extend([self.person])
				#call the random room allocator.
				#pass the person instance variables.
				if self.jobType == "FELLOW" and self.wantsRoom == "YES":
					if self.randomOfficeAllocator(self.name) == True:
						print 
						self.randomRoomAllocator(
							self.person.name,self.person.jobType,self.person.wantsRoom,self.person.id_no)
						
				else:
					self.randomRoomAllocator(
						self.person.name,self.person.jobType,self.person.wantsRoom,self.person.id_no)
			
			else:
				print "Be safe at where you will stay.\n"	

	def randomOfficeAllocator(self, name = ""):
		#Set list of all rooms that are office.
		self.offices = []
		self.value = False

		for rooms in range(0, len(Storage.list_of_all_rooms)):
			if Storage.list_of_all_rooms[rooms].room_type == "OFFICE":
				self.offices.append(Storage.list_of_all_rooms[rooms])
				print "awesome."

		#Do random 
		if len(self.offices) > 0:
			try:
				for rooms in range(len(self.offices)):
					room = self.offices[random.randint(0,len(self.offices)-1)]
					if self.offices[rooms].room_instance.isFull() != True:
						self.offices[rooms].room_instance.current_members.append(name)
						print "Your room allocation has been successfull!!"
						print "Your office space is in {}.".format(self.offices[rooms].room_name)
						self.value = True
						break
			except Exception as e:
				print "No offices available. sorry."			
		else:
			print "No offices available. Sorry."

		print self.value	
		return self.value							
	"""
	Create new instance of room depending on the jobtype
	and allocate the person to that room.

	All this is at random. 
	"""	

	"""
	@Change
	call this method with the instance of person as the argument
	rather than using name,jobtype and wantsroom of that instance.

	For now use as it is...
	"""
	def randomRoomAllocator(self,name,jobType,wantsRoom,id_no):
		self.name = name
		self.jobType= jobType.upper()
		self.wantsRoom = wantsRoom
		self.id_no = id_no

		self.incrementor +=1
		"""
		@Question
		Can a fellow be allocated either office or livingspace?
			1. Check room is available
			2. Room is not full
		"""
		RoomToPerson = {"OFFICE":"STAFF", "LIVINGSPACE":"FELLOW"}

		#Select room at random.
		randomRoom = Storage.list_of_all_rooms[random.randint(
			0,len(Storage.list_of_all_rooms)-1)]

		#check if the room select is office,staff can be allocated.
		#and if livingspace, only fellows are allocated.

		#Check number of people in the system doesn't pass the available room spaces
		if len(Storage.people_info) <= Storage.total_no_of_rooms and Storage.total_no_of_rooms > 0:
			if RoomToPerson[randomRoom.room_type] == self.jobType:
				#check the room is not full 

				if randomRoom.room_instance.isFull() == True:
					if self.incrementor < 15:
						self.randomRoomAllocator(
							self.name, self.jobType, self.wantsRoom,self.id_no)
					else:
						if self.backup(self.name, self.jobType,self.wantsRoom, self.id_no) == False:
							Storage.list_of_unallocated_people.append(self.id_no)
							Storage.unallocated_people_info[self.id_no] = self.name

							print "Sorry!! We couldn't find you a room." 
							print "Your ID is {}. Keep it safe.".format(self.id_no)
							print "We will let you know, when room is free."


				else:
					#allocate the person room.
					#check the person is not already allocated room.Doesn't exist in the system
					if not Storage.people_info.has_key(self.id_no):
						randomRoom.allocate_member_a_room(self.name,self.id_no,self.jobType)


					else:
						#print "The person has room already allocated."
						if self.incrementor < 15:
							self.randomRoomAllocator(
								self.name, self.jobType, self.wantsRoom, self.id_no)
						else:
							if self.backup(self.name, self.jobType, self.wantsRoom, self.id_no) == False:
								Storage.list_of_unallocated_people.append(self.id_no)
								Storage.unallocated_people_info[self.id_no] = self.name

								print "Sorry!! We couldn't find you a room." 
								print "Your ID is {}. Keep it safe.".format(self.id_no)
								print "We will let you know, when room is free."
							else:
							
								return "Your room allocation has been successfully!!"	
		

			else:
				#incrementor can be any number. default is 15.
				if self.incrementor < 15 :

					self.randomRoomAllocator(
						self.name, self.jobType, self.wantsRoom,self.id_no)	
				
				elif self.incrementor == 15:
					if self.backup(self.name, self.jobType,self.wantsRoom, self.id_no) == False:
						Storage.list_of_unallocated_people.append(self.id_no)
						Storage.unallocated_people_info[self.id_no] = self.name

						print "Sorry!! We couldn't find you a room." 
						print "Your ID is {}. Keep it safe.".format(self.id_no)
						print "We will let you know, when room is free."
					else:
						
						return "Your room allocation has been successfully!!"	

				else:
					#Store only id number for the person
					#value = "Name :",self.name," Id number : ",self.id_no

					Storage.list_of_unallocated_people.append(self.id_no)
					Storage.unallocated_people_info[self.id_no] = self.name

					print "Sorry!! We could find you a room." 
					print "Your ID is {}. Keep it safe.".format(self.id_no)
					print "We will let you know, when room is free."


		else:
			#Add the person to unallocated list of people.

			#value = "Name :",self.name," Id number : ",self.id_no
			Storage.list_of_unallocated_people.append(str(self.id_no))
			Storage.unallocated_people_info[self.id_no] = self.name

			print "Sorry!! We could find you a room." 
			print "Your ID is "+self.id_no+". Keep it safe."
			print "We will let you know, when room is free."



	"""
	Check that the person with that id number exists in the system
	and has already accomodation. 
	
	Check type of his/her job and reallocate him/her to an existing 
	room of same type thats is not full.

	Can only allocate to room of the same type.
	"""	
	def backup(self,name, jobtype,wantsroom, id_no):
		self.name = name
		self.jobtype = jobtype
		self.wantsroom = wantsroom
		self.id_no = id_no

		result = False

		for rooms in range(len(Storage.list_of_all_rooms)):
			roomInstance = Storage.list_of_all_rooms[rooms]
			roomType = Storage.list_of_all_rooms[rooms].room_type
			isFull = Storage.list_of_all_rooms[rooms].room_instance.isFull()
			members = Storage.list_of_all_rooms[rooms].room_instance.current_members
			if roomType == self.jobtype and isFull == False:
				if not Storage.people_info.has_key(self.id_no):
					roomInstance.allocate_member_a_room(self.name,self.id_no. self.jobtype)
					result = True
					break

		return result		


	def reallocate_person(self, id_no = 0, new_room_name = ""):
		self.id_no = id_no
		self.name_of_id_owner = ""
		self.new_room_name = new_room_name.upper()

		self.new_room_type = None
		self.new_room_members = None

		#Deal with new room stuff.
		for rooms in range(len(Storage.list_of_all_rooms)):
			if Storage.list_of_all_rooms[rooms].room_name == self.new_room_name:
				self.new_room_type = Storage.list_of_all_rooms[rooms].room_type
				self.new_room_members = Storage.list_of_all_rooms[rooms].room_instance.current_members
			else:
				continue

		#Deal with id stuff		
		if Storage.people_info.has_key(int(self.id_no)):
			self.name_of_id_owner = Storage.people_info[int(self.id_no)]


		#Reallocate person.
		try:
			self.value = ""
			for rooms in range(0, len(Storage.list_of_all_rooms)):
				if self.name_of_id_owner in Storage.list_of_all_rooms[rooms].room_instance.current_members:

					Storage.list_of_all_rooms[rooms].room_instance.current_members.remove(self.name_of_id_owner)
					self.value +=" You are being removed from {}".format(Storage.list_of_all_rooms[rooms].room_name)
					break

			for rooms in range(0, len(Storage.list_of_all_rooms)):
				if Storage.list_of_all_rooms[rooms].room_name != self.new_room_name \
				and Storage.list_of_all_rooms[rooms].room_type == self.new_room_type:

					self.new_room_members.append(self.name_of_id_owner)
					self.value +=" and taken to {}.".format(Storage.list_of_all_rooms[rooms].room_name)
					break
			print self.value		
		except Exception as e:
			print "Sorry!! An error has occured. Try again later"	
						

				
	"""
	Load all people from a file. and does the allocations.
	"""

	def load_people(self,filename):
		self.filename = filename
		#Check file name extension.
		if self.filename[-3:].upper() != 'TXT':
			self.filename+='.txt'
		#Check file exists in the directory.
		if os.path.exists(self.filename):
			with open(self.filename) as file:
				for lines in file:
					content = lines.split()
					if len(content) == 3:
						content.extend("NO")

					name = content[0]+" "+content[1]
					job = content[2]
					wantsroom = content[3] or "NO"
					print "\t{} {} {}".format(name,job,wantsroom)
					self.allocateRoom(name,job,wantsroom)
		else:
			
			print "No file with that name exist."			

	"""
	Print unallocated people.
	"""
	def unallocated_people(self, filename):
		self.filename = filename
		if self.filename == "":
			print "This data is not being written to any text file."
		else:
			print "This information is being saved to text file called '{}'".format(
				self.filename)	
		#Check file name extension.
		if self.filename[-3:].upper() != 'TXT':
			self.filename+='.txt'
		#Check file exists in the directory.
		if not os.path.exists(self.filename):
			self.file = open(self.filename,'w') 
		else:
			self.file = open(self.filename,'w')

		if len(Storage.list_of_unallocated_people)>0:
			for unallocated in range(len(Storage.list_of_unallocated_people)):
				value = Storage.list_of_unallocated_people[unallocated]
				result = "{}. {} \n".format(
					unallocated+1,Storage.unallocated_people_info[value])
				self.file.write(result)
				print result
		else:
			value = "Hurray!!\nNo one is on the waiting list."
			self.file.write(value)
			print value
		self.file.close()	

		
	"""
	Save all content on an sqlite specified database
	if create a new sqlite db of name wanted.
	"""
	def save_state(self, database = "sqlite.db"):
		self.db.Save(database)	


	"""
	Load all content from db given. 
	"""
	def load_state(self,database = "sqlite"):
		self.db.Load(database)


	def allocated_people(self, filename):
		self.filename = filename
		#Check file name extension.
		if self.filename[-3:].upper() != 'TXT':
			self.filename+='.txt'
		#Check file exists in the directory.
		if not os.path.exists(self.filename):
			self.file = open(self.filename,'w') 
		else:
			self.file = open(self.filename,'w')
			
		#Write on the file.
		if len(Storage.list_of_all_rooms)>0:
			for size in range(len(Storage.list_of_all_rooms)):
				value = "\tRoom name :\t {}\n\tRoom type :\t {}\n".format(
					Storage.list_of_all_rooms[size].room_name,
					Storage.list_of_all_rooms[size].room_type)
				self.file.write(value)
				print value
				self.file.write("-"*60)
				self.file.write("\n")
				print "-"*60
				#Check the room is not empty
				if len(Storage.list_of_all_rooms[size].room_instance.current_members)>0:
					for member in range(len(
						Storage.list_of_all_rooms[size].room_instance.current_members)):
						value = "\t{}. {}".format(member+1,
							Storage.list_of_all_rooms[size].room_instance.current_members[member])
						self.file.write(value)
						self.file.write(" \n")
						print value+" \n"
					self.file.write(" \n \n")
						 
				else:
					value = "No members currently allocated this room.\n\t\tSad :( "
					self.file.write(value)
					self.file.write(" \n \n")
					print value+" \n \n"
			self.file.close()		
							
		else:
			print "No existing rooms to allocate anyone."


	def print_rooms(self, room_name):
		self.room_name = room_name.upper()
		self.value = False
		for size in range(len(Storage.list_of_all_rooms)):
			if self.room_name == Storage.list_of_all_rooms[size].room_name:
				self.value = True
				if len(Storage.list_of_all_rooms[size].room_instance.current_members) > 0:
					for rooms in range(
						0, len(
							Storage.list_of_all_rooms[size].room_instance.current_members)):
						print "{}. {}".format(
							rooms+1, Storage.list_of_all_rooms[size].room_instance.current_members[rooms])

				else:
					print "Room is empty."
					break
					return None		
			else:
				if size+1 == len(Storage.list_of_all_rooms) and self.value == False:
					print "Sorry!! That room doesn't exist."
					break	
					return None			
					


