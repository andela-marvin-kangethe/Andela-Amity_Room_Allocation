from app.staff import Staff
from app.storage import Storage
import unittest
from mock import patch, Mock


class Test(unittest.TestCase):

    def setUp(self):
        self.staff = Staff()

    def test_id_value(self):
        self.assertNotEqual(self.staff.id_no, 0, msg="Id number not sumitted.")

    @patch('app.storage')
    def test_staff_has_office_allocation(self,test_storage):
    	test_storage.people_info.retun_value = {12345678 :"Marvin kangethe"}
    	self.assertTrue(self.staff.is_allocated(12345678), msg = "You already have room allocated.")
  
 