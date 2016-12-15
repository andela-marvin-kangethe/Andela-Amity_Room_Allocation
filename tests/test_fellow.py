from app.fellow import Fellow
from app.storage import Storage

import unittest
from mock import patch, Mock


class TestFellow(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow()
        self.fellow.id_no = 1234

    def test_id_value(self):
        self.assertNotEqual(self.fellow.id_no, 0)

    def test_id_type(self):    
    	self.assertEqual(type(self.fellow.id_no), int)

    def test_id_size(self):	
    	self.assertEqual(len(str(self.fellow.id_no)), 4)

    @patch('app.storage')
    def test_fellow_has_office_allocation(self,test_storage):
    	Storage.people_info = {1234 :"Marvin kangethe"}
    	self.assertTrue(self.fellow.is_allocated(self.fellow.id_no))


if __name__ == '__main__':
    unittest.main()        

    	
    	