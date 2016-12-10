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
	def createRoom(self,room_name = ""):
		self.room_name = room_name.upper()
		result = False
		Result = ""

		for rooms in range(len(Storage.list_of_all_rooms)):
			if self.room_name == Storage.list_of_all_rooms[rooms].Room_name:
				#Check that the room already exist.
				result = True

		if  self.room_name != "" and result != True :#:
			#Create instance of room class
			room_type = random.choice(["OFFICE","LIVINGSPACE"])
			self.room = Room(self.room_name, room_type)

			#Save instance of room in list of all rooms

			Storage.list_of_all_rooms.append(self.room)	

			value = "\t{}\t\t[ {} ]\tcreated successfully!!".format(self.room.Room_name, self.room.Room_type)
			Result =  "Room created successfully!!"
		else:
			value =  "Room called {} failed to create.".format(self.room.Room_name)
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
				self.randomRoomAllocator(
					self.person.name,self.person.jobType,self.person.wantsRoom,self.person.id_no)
			
			else:
				print "Be safe at where you will stay.\n"	

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
			if RoomToPerson[randomRoom.Room_type] == self.jobType:
				#check the room is not full 

				if randomRoom.Room_instance.isFull() == True:
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
						randomRoom.allocate_member_a_room(self.name,self.id_no)

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
			roomType = Storage.list_of_all_rooms[rooms].Room_type
			isFull = Storage.list_of_all_rooms[rooms].Room_instance.isFull()
			members = Storage.list_of_all_rooms[rooms].Room_instance.current_members
			if roomType == self.jobtype and isFull == False:
				if not Storage.people_info.has_key(self.id_no):
					roomInstance.allocate_member_a_room(self.name,self.id_no)
					result = True
					break

		return result		


	def reallocate_person(self,id_no = 0,New_Room_name = ""):
		self.id_no = id_no
		self.New_Room_name = New_Room_name.upper()
		"""
		1.	Check if the id provided is in the people info dictionary
			and the person is not already allocated to the room he/she
			wants reallocation to.
		"""

		if Storage.people_info.has_key(self.id_no):
			"""
			2. Check if the room he/she wants allocation to exist
			"""
			if Storage.people_info[self.id_no] not in Storage.list_of_unallocated_people:

				for rooms in range(
					0, len(Storage.list_of_all_rooms)):
					if Storage.list_of_all_rooms[rooms].Room_name == self.New_Room_name:
						"""
						3.	Check if there is a room available for rellocation
							3a. Get the job type of the person with the id
						"""
						for room in range(
							0, len(Storage.list_of_all_rooms)):
							if Storage.people_info[self.id_no] in Storage.list_of_all_rooms[room].Room_instance.current_members:
								#print ">> Moving "+Storage.people_info[self.id_no]+" to ",Storage.list_of_all_rooms[room].Room_type 
								"""
								3b. Check all rooms that are offices and not full and not the same room.
								"""
								my_room = Storage.list_of_all_rooms[rooms].Room_name
								my_room_type = Storage.list_of_all_rooms[rooms].Room_type
								my_room_mates = Storage.list_of_all_rooms[rooms].Room_instance.current_members

								for otherRooms in range(len(Storage.list_of_all_rooms)):
									if  Storage.list_of_all_rooms[otherRooms].Room_name != my_room \
										and Storage.list_of_all_rooms[otherRooms].Room_type == my_room_type \
										and Storage.list_of_all_rooms[otherRooms].Room_instance.isFull() != True \
										and Storage.people_info[self.id_no] in my_room_mates:

										print "Current room is {}.and i passed {}".format(my_room, self.New_Room_name)
										print ">>> Moving you to {}".format(Storage.list_of_all_rooms[otherRooms].Room_name)

										print Storage.people_info," ",self.New_Room_name," ",Storage.people_info[self.id_no]," ",my_room_mates
											
										my_room_mates.remove(Storage.people_info[self.id_no])
										Storage.list_of_all_rooms[otherRooms].Room_instance.current_members.append(Storage.people_info[self.id_no])
										print  "Reallocation successfull!! "
										return "Reallocation successfull!! "
									else:
										if otherRooms+1 == len(Storage.list_of_all_rooms):
											print Storage.people_info," ",self.New_Room_name," ",Storage.people_info[self.id_no]," ",my_room_mates
											print "Sorry!! We can't reallocate you at the current time."
										else:
											continue	
							else:
								if room+1 == len(Storage.list_of_all_rooms):
									break
									#print "No person with that id is allocated a room."
								else:
									continue	

										#Now remove person in original room and add in the new room current members.
					else:
						continue
						#print "No room with that name exists."
			else:
				print "You have not been allocated room yet."
				print "Wait until have room allocation."				
		else:
			print "Invalid id number provided."
			print "Provide correct details and try again."	
		return ""
				
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
	def save_state(self, database = "sqlite_db"):
		self.db.Save(database)	


	"""
	Load all content from db given. 
	"""
	def load_state(self,database):
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
				value = "\tRoom name :\t {}\n".format(
					Storage.list_of_all_rooms[size].Room_name)
				self.file.write(value)
				print value
				self.file.write("-"*60)
				self.file.write("\n")
				print "-"*60
				#Check the room is not empty
				if len(Storage.list_of_all_rooms[size].Room_instance.current_members)>0:
					for member in range(len(
						Storage.list_of_all_rooms[size].Room_instance.current_members)):
						value = "\t{}. {}".format(member+1,
							Storage.list_of_all_rooms[size].Room_instance.current_members[member])
						self.file.write(value)
						self.file.write(" \n")
						print value+" \n"
					self.file.write(" \n")
						 
				else:
					value = "No members currently allocated this room.\n\t\tSad :( "
					self.file.write(value)
					self.file.write(" \n \n")
					print value+" \n \n"
			self.file.close()		
							
		else:
			print "No existing rooms to allocate anyone."



		#Write on the 			


	
	def print_rooms(self, room_name):
		self.room_name = room_name.upper()
		for size in range(len(Storage.list_of_all_rooms)):
			if self.room_name == Storage.list_of_all_rooms[size].Room_name:
				if len(Storage.list_of_all_rooms[size].Room_instance.current_members) > 0:
					for rooms in range(
						0, len(
							Storage.list_of_all_rooms[size].Room_instance.current_members)):
						print "{}. {}".format(
							rooms+1, Storage.list_of_all_rooms[size].Room_instance.current_members[rooms])
				else:
					print "Room is empty."
					break
					return None		
			else:
				if size+1 == len(Storage.list_of_all_rooms):
					print "Sorry!! That room doesn't exist."
					break	
					return None			
					
if __name__ == '__main__':
	store = Storage()
 	amity = Amity()

 	amity.createRoom("Hogwards")
 	amity.createRoom("Narnia")

 	amity.allocateRoom("marvin kang","FELLOW","YES")
 	
 	amity.reallocate_person(1234, "Hogwards")

# 	amity.createRoom("Camelot")
# 	amity.createRoom("Mordor")

# 	for size in range(len(store.list_of_all_rooms)):
# 		print store.list_of_all_rooms[size].Room_name
"""
	
 	amity.allocateRoom("Steve jobs1","staff","yes")
 	amity.allocateRoom("Steve jobs2","staff","yes")
 	amity.allocateRoom("Steve jobs3","staff","yes")
 	amity.allocateRoom("Steve jobs4","staff","yes")
 	amity.allocateRoom("Steve jobs5","staff","yes")
 	amity.allocateRoom("Steve jobs6","staff","yes")
 	amity.allocateRoom("Steve jobs7","staff","yes")

	amity.print_rooms("Hogwards")
	print "Start unallocation"
	amity.unallocated_people("Amity.txt")
"""
	# print "Time for reallocations"
	# amity.reallocate_person(1234,"NARNIA")
	# amity.print_rooms("NARNIA")
 		

# 	for rooms in range(len(store.list_of_all_rooms)):
# 		print "\n\tName of room :\t", store.list_of_all_rooms[rooms].Room_name
# 		print "\tType of room :\t", store.list_of_all_rooms[rooms].Room_type
# 		print "\tCurrent occupants:\t", len(store.list_of_all_rooms[rooms].Room_instance.current_members)

# 		for size in range(len(store.list_of_all_rooms[rooms].Room_instance.current_members)):
# 			print store.list_of_all_rooms[rooms].Room_instance.current_members[size]
		
# 	amity.unallocated_people()

# 	key = [key for key, value in Storage.people_info.items() if value == "Steve jobs"]
# 	result = 0
# 	for size in range(len(key)):
# 		result = int(key[size])

# 	print result
# 	amity.reallocate_person(result, "Mordor")


# 	for rooms in range(len(store.list_of_all_rooms)):
# 		print "\n\tName of room :\t", store.list_of_all_rooms[rooms].Room_name
# 		print "\tType of room :\t", store.list_of_all_rooms[rooms].Room_type
# 		print "\tCurrent occupants:\t", len(store.list_of_all_rooms[rooms].Room_instance.current_members)

# 		for size in range(len(store.list_of_all_rooms[rooms].Room_instance.current_members)):
# 			print store.list_of_all_rooms[rooms].Room_instance.current_members[size]