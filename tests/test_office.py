from app.office import Office
import unittest


class Test(unittest.TestCase):
	
	def setUp(self):
		self.office = Office()

	def test_office_is_not_full(self):
		result = self.office.isFull()
		self.assertEqual(result, False, msg = "The office is now full")	