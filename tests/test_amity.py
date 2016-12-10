from app.amity import Amity
import unittest
from mock import Mock,patch

class TestAmity(unittest.TestCase):
	"""docstring for Test"""

	#Create instance of Amity
	def setUp(self):
		self.amity = Amity()
	
	@patch('app.storage')	
	def test_room_creation(self,test_storage):
		test_storage.list_of_all_rooms.return_value = ["CAMELOT","NARNIA"]
		result = Mock()
		result.room_name.return_value = "HOGWARDS"
		print test_storage.list_of_all_rooms.return_value
		self.result = self.amity.createRoom(result.room_name.return_value)
		print self.amity.room_name
		print test_storage.list_of_all_rooms.return_value

		if self.result != "Room created successfully!!":
			self.assertNotEqual(
				self.amity.room_name, "", msg = "Cannot create empty room")

			self.assertNotIn(
				self.amity.room_name,
				test_storage.list_of_all_rooms.return_value,
				msg = "Room with that name already exist."
				)
			print test_storage.list_of_all_rooms.return_value
		else:
			self.assertIn(
				self.amity.room_name,
				test_storage.list_of_all_rooms.return_value,
				msg = "Room with that name already exist."
				)	


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