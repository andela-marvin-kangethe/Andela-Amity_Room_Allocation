from app.room import Room
from app.storage import Storage
from app.person import Person
import unittest
from mock import Mock, patch

class Test(unittest.TestCase):
	
	def setUp(self):
		self.room = Room("Hogwards")

	def test_room_name_and_type(self):
		self.assertNotEqual(self.room.Room_name, "", msg = "Cannot create empty room.")
		self.assertIn(
			self.room.Room_type.upper(),["OFFICE","LIVINGSPACE"], msg = "Room can be office or living space.")
	"""
	@patch('app.storage')
	def test_room_reallocation_variables(self,test_storage):
		self.room.reallocate_person()
		result = Mock()
		result.id_no.return_value = 12345678
		result.New_Room_name.return_value = "Hogwards"
		self.assertNotEqual(self.room.id_no, 0, msg= "Invalid id number submitted.")
		self.assertNotEqual(self.room.New_Room_name, "", msg  = "The room does not exist.")
		#test_storage.people_info.return_value = {12345678:"Marvin Kangethe", 98765432:"John Doe"}
			
		
	@patch('app.person')
	@patch('app.office')
	@patch('app.livingspace')
	def test_successful_room_reallocation(self,test_person,test_office,test_livingspace):
		test_person.name.return_value = "Marvin Kangethe"
		test_office.current_members.return_value = ["Marvin Kangethe","John Doe"]
		test_livingspace.current_members.return_value = test_office.current_members.return_value
		result = test_livingspace.current_members.return_value
		if self.room.reallocate_person() == "Person reallocation successfull!!":
			self.assertNotIn(
				test_person.name, self.room.Room_instance.current_members, msg = "The person is already allocated room somewhere else")
		else:
			print "Check something"
	"""

	@patch('app.storage')	
	def test_new_room_exist(self,test_storage):
		test_storage.list_of_all_rooms.return_value = ["Hogwards","Camelot","Narnia"]
		result_mock = Mock()
		result_mock.New_Room_name.return_value = "Hogwards"
		self.assertIn(
			result_mock.New_Room_name.return_value,test_storage.list_of_all_rooms.return_value,msg = "The rooms does not exist.")

	@patch('app.storage')	
	@patch('app.person')
	def test_room_allocation(self,test_storage,test_person):
		test_person.name.return_value = "Alex Kang"
		test_person.id_no.return_value = 39090901
		test_storage.people_info.return_value = {
			12345678:"Marvin Kangethe", 98765432:"John Doe"}
		test_storage.list_of_all_rooms.return_value = ["Hogwards","Camelot","Narnia"]
		
		self.room.allocate_member_a_room(
			test_person.name.return_value, test_person.id_no.return_value)
		#print test_storage.people_info.return_value
		#self.assertTrue(
		#	bool(test_storage.people_info.return_value.has_key(
		#		test_person.id_no.return_value)), msg = "The person hasn't been added yet.")
		self.assertFalse(
			test_storage.people_info.return_value.has_key(
				test_person.id_no.return_value), msg = "Person has room already allocated.")
		

		
if __name__ == '__main__':
		unittest.main()	











