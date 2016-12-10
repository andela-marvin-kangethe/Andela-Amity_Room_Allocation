from app.fellow import Fellow
from app.storage import Storage

import unittest
from mock import patch, Mock


class Test(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow()

    def test_id_value(self):
        self.assertNotEqual(self.fellow.id_no, 0, msg="Id number not sumitted.")

	@patch('app.storage')
	def test_fellow_has_room_allocation(self,test_storage):
		test_storage.people_info.retun_value = {12345678 : "Marvin kangethe"}
		self.assertTrue(self.fellow.is_allocated(12345678), msg = "You already have room allocated.")
  
 