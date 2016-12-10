from app.office import Office
from app.livingspace import LivingSpace

from app.storage import Storage

import random 

class Room(Storage):
	"""docstring for Room"""
	"""
	The length of this list cannot be more 
	than the number of total rooms
	"""
	List_of_all_members = []

	def __init__(self, Room_name = "",Room_type = ""):
		self.Room_name = Room_name
		self.Room_type = Room_type
		
		#Create a variable that holds the instance of the room type created.

		if self.Room_type == "OFFICE":
			self.Room_instance =  Office(self.Room_name)

			Storage.total_no_of_rooms +=6
			#Increment number of total room spaces by 4 for every office created.
		elif self.Room_type == "LIVINGSPACE":
			self.Room_instance =  LivingSpace(self.Room_name)

			Storage.total_no_of_rooms +=4
			#Increment number of total room spaces by 6 for every living space created.

		else:
			#Do nothing if room is neither office or livingspace
			self.Room_instance =  LivingSpace(self.Room_name)
			Storage.total_no_of_rooms +=4
			#Increment number of total room spaces by 6 for every living space created.




	"""
	Allocate a person to a room at random depending on if the person 
	wants allocation{ also yes for staff }. 
	check if room is full.
		NB
			fellow are allocated either office or living space
			staff are allocated only office.
	"""	
	def allocate_member_a_room(self,name = "",id_no = 0):
		self.name = name
		self.id_no = id_no

		#1. Add to the list of current occupents in the room instance

		#value = "NAME :",self.name," ID :",self.id_no
		self.Room_instance.current_members.append(self.name)

		#2. Add person to the amity people info 
		#KEY : ID number, VALUE : NAME

		Storage.people_info[self.id_no] = self.name

		# print self.name," added to the system.In room : ",self.Room_name
		# for size in range(len(self.Room_instance.current_members)):
		# 	print self.Room_instance.current_members[size]

		print "Your room allocation has been successfully!!"
		print "Your room space is in {}.".format(self.Room_name)
		print "Your ID number is {}.".format(self.id_no)
		print "Keep it safe and Welcome to the Dojo!!\n"
		return "Your room allocation has been successfully!!"




















		

	
