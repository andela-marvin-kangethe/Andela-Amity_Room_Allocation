from app.amity import Amity
import unittest
from app.storage import Storage
from mock import Mock,patch

class TestAmity(unittest.TestCase):
	"""docstring for Test"""

	#Create instance of Amity
	def setUp(self):
		self.amity = Amity()
	
	def test_room_creation(self):
		size = len(Storage.list_of_all_rooms)
		if self.amity.createRoom("Hogwards") == "Room created successfully!!":

			self.assertEqual(len(Storage.list_of_all_rooms), size+1)
		else:
		
			self.assertEqual(len(Storage.list_of_all_rooms), size)
	
	def test_room_allocation(self):
		size = len(Storage.people_info)

		if self.amity.allocateRoom(
			" Marvin Jones","FELLOW","YES") == "Your room allocation has been successfully!!":

			self.assertEqual(len(Storage.people_info), size +1)


	def test_room_reallocation(self):
		size = len(Storage.people_info)

		if self.amity.allocateRoom(
			1234, "Hogwards") == "Reallocation successfull!! ":

			self.assertTrue(Storage.people_info.has_key(1234))
			self.assertEqual(len(Storage.people_info), size)
		else:
		
			self.assertFalse(Storage.people_info.has_key(1234))
			self.assertEqual(len(Storage.people_info), size)

	# def test_room_allocation(self):
	# 	self.result = self.amity.allocateRoom("","")

	# 	if self.result != "Room allocation successfully!!":

	# 		self.assertIn(self.amity.jobType.upper(),["FELLOW","STAFF"],msg = "Cannot allocate room to person whom is not STAFF or FELLOW.")

	# 		self.assertNotEqual(self.amity.name,"",msg = "Cannot allocate empty person a room")

	# 		self.assertIn(self.amity.name, self.amity.list_of_unallocated_people, msg = "Person must be in waiting list!!")

	# 		self.assertIn(self.amity.wantsRoom.upper(),["Y","YE","YES","N","NO"], msg = "Use YES or NO to select if you want room allocation")


	def test_load_people(self):
		pass

	
	def test_save_state(self):
		pass

	
	def test_load_state(self):
		pass		
			

if __name__ == '__main__':
	
	unittest.main()		