from app.staff import Staff
from app.storage import Storage
import unittest
from mock import patch, Mock


class TestStaff(unittest.TestCase):

    def setUp(self):
        self.staff = Staff()
        self.staff.id_no = 1234

    def test_id_value(self):
        self.assertNotEqual(self.staff.id_no, 0, msg="Id number not sumitted.")

    def test_id_type(self):    
    	self.assertEqual(type(self.staff.id_no), int)

    def test_id_size(self):	
    	self.assertEqual(len(str(self.staff.id_no)), 4)

    @patch('app.storage')
    def test_staff_has_office_allocation(self,test_storage):
    	Storage.people_info = {1234 :"Marvin kangethe"}
    	self.assertTrue(self.staff.is_allocated(self.staff.id_no))

if __name__ == '__main__':
    unittest.main()    	