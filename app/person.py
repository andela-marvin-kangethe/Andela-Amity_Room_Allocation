from app.storage import Storage

from app.staff import Staff
from app.fellow import Fellow

import random 


class Person(Storage):
	"""docstring for Person"""
	def __init__(self,name="",jobType = "",wantsRoom = "NO",choice = 1,new_id_no = 0):
		self.name = name
		self.jobType = jobType
		self.wantsRoom = wantsRoom
		self.choice = choice
		self.id_no = 0
		self.new_id_no = new_id_no

		if self.choice == 0:
			#self.id_no = 1234
			self.id_no = self.generate_ID(self.name)
		else:
			self.id_no = self.new_id_no	

		#Create a variable that holds the instance of person created
		if self.jobType == "FELLOW":
			self.andelan = Fellow(self.id_no)

		elif self.jobType == "STAFF":
			self.andelan = Staff(self.id_no)

		else:
			#If job type is not indicated, person created is fellow by default.
			self.wantsRoom = "NO"
			self.andelan = Fellow(self.id_no)	
	


	"""
	Auto generate ID numbers for the person created.
	The id number should be random of length 6. 
	Check that the value does not already exist.
	"""
	def generate_ID(self,name = ""):
		self.name = name
		#Generate a 6 lenght integer value that doesn't ready exist in the system

		randomValue = random.randint(1000, 9999)

		if Storage.people_info.has_key(randomValue):
			#Reran the function again.
			#Until a unique value that doesn't exist in the system is found. 
			self.generate_ID(self.name)
		else:
			
			return randomValue	


	"""
	Check if there are available rooms left and assign room to person
	depending on 	
		1. If the person wants the room { staff cannot refuse room allocation }
		2. If there are available rooms left 
	
	Add member to dictionary containing id_no as key, and name as value,
			{ multiple names can be the same but id_no cannot}
	"""	

	def add_member_to_system(self):
		#Check that the id doesn't exist in the people info

		if Storage.people_info.has_key(self.id_no):
			print "Person already exist in th system."
		else:
			Storage.people_info[self.id_no] = self.name

			print "Person added successfully."	




	
		
