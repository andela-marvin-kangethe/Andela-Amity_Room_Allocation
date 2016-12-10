from app.person import Person
from app.storage import Storage
import unittest  
from mock import Mock, patch


class Test(unittest.TestCase):
	
	def setUp(self):
		self.person = Person("Marvin","FELLOW","YES")

	def test_instance_valriables(self):
		self.assertNotEqual(self.person.name,"",msg = "Invalid name credentials.")	
		self.assertIn(
			self.person.jobType.upper(),
			["STAFF","FELLOW"],msg = "Person can only be STAFF or FELLOW")	
		self.assertIn(
			self.person.wantsRoom.upper(),
			["Y","YE","YES","N","NO"], msg = "Use only YES or NO.")

	@patch('app.storage')	
	def test_person_not_in_system(self,test_storage):
		test_storage.people_info.return_value = {12345678 : "marvin kangethe", 98765432 : "john doe"}
		self.person.id_no = 22345678
		self.assertEqual(
			type(self.person.id_no),
			int, msg = "ID numbers must have an integer format.")
		
		self.assertFalse(
			bool(test_storage.people_info.return_value.has_key(self.person.id_no)),
			msg = "Person already in the system.")
 
		
	@patch('app.storage')
	def test_add_member_to_system(self,test_storage):
		test_storage.people_info.return_value = {12345678 : "Marvin Kangethe", 98765432 : "John Doe"}
		result = self.person.add_member_to_system()

		if result == "Member added successfully":
			self.assertTrue(test_storage.people_info.has_key(self.person.id_no),msg = "The person hasn't been added  yet.")
		else:
			self.assertNotEqual(self.person.name, "", msg = "Cannot add an empty person to the system.")
			self.assertNotEqual(self.person.id_no, 0, msg = "Cannot add a person without valid ID to the system.")
			self.assertTrue(test_storage.people_info.has_key(self.person.id_no), msg = "The person cannot be added to the system.")	

if __name__ == '__main__':
	unittest.main()