from app.person import Person
from app.storage import Storage
import unittest  
from mock import Mock, patch


class TestPerson(unittest.TestCase):
	
	def setUp(self):
		self.person = Person("Marvin","FELLOW","YES")
		self.person.id_no = 2234

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
		#test_storage.people_info.return_value = {12345678 : "marvin kangethe", 98765432 : "john doe"}

		Storage.people_info = {1234 : "marvin kangethe", 9876 : "john doe"}
		
		
		self.assertEqual(
			type(self.person.id_no),int)
		
		self.assertFalse(
			bool(Storage.people_info.has_key(self.person.id_no)))
 
		
	@patch('app.storage')
	def test_add_member_to_system(self,test_storage):
		#test_storage.people_info.return_value = {12345678 : "Marvin Kangethe", 98765432 : "John Doe"}
		
		Storage.people_info = {1234 : "Marvin Kangethe", 9876 : "John Doe"}
		result = self.person.add_member_to_system()

		if result == "Member added successfully":
			self.assertTrue(Storage.people_info.has_key(
				self.person.id_no))
		else:
			self.assertNotEqual(
				len(self.person.name), 0)
			
			self.assertNotEqual(
				self.person.id_no, 0)
			
			self.assertTrue(
				Storage.people_info.has_key(self.person.id_no))	

if __name__ == '__main__':
    unittest.main()








