from app.room import Room
from app.storage import Storage
from app.person import Person
import unittest
from mock import Mock, patch

class TestRoom(unittest.TestCase):
	
	def setUp(self):
		
		self.room = Room("Hogwards","OFFICE")

	def test_room_name_and_type(self):
		self.assertNotEqual(self.room.Room_name, "", msg = "Cannot create empty room.")
		self.assertIn(
			self.room.Room_type.upper(),["OFFICE","LIVINGSPACE"], msg = "Room can be office or living space.")
	
	@patch('app.storage')	
	def test_new_room_exist(self,test_storage):
		Storage.list_of_all_rooms = ["HOGWARDS","CAMELOT","NARNIA"]
 	 	# test_storage.list_of_all_rooms.return_value = ["Hogwards","Camelot","Narnia"]
	  	# result_mock = Mock()
	 	# result_mock.New_Room_name.return_value = "Hogwards"
		self.assertIn(
			self.room.Room_name.upper(),Storage.list_of_all_rooms,msg = "The rooms does not exist.")

	@patch('app.storage')	
	@patch('app.person')
	def test_room_allocation(self,test_storage,test_person):
		Storage.people_info = {}
		# test_person.name.return_value = "Alex Kang"
		# test_person.id_no.return_value = 3909
		# test_storage.people_info.return_value = {
		# 	12345678:"Marvin Kangethe", 98765432:"John Doe"}
		# test_storage.list_of_all_rooms.return_value = ["Hogwards","Camelot","Narnia"]
		
		if self.room.allocate_member_a_room(
			"Alex kang", 3909) == "Your room allocation has been successfully!!":
			
			self.assertTrue(
				bool(Storage.people_info.has_key(
					self.room.id_no)), msg = "The person hasn't been added yet.")
		 	
		 	self.assertEqual(Storage.people_info[self.room.id_no], self.room.name)

		 	self.assertIn(self.room.name, self.room.Room_instance.current_members)
		
		else:
		 		
		 	self.assertFalse(
				bool(Storage.people_info.has_key(
					self.room.id_no)), msg = "The person hasn't been added yet.")

if __name__ == '__main__':
    unittest.main()







