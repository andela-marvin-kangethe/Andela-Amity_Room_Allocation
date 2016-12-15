from app.office import Office
import unittest


class TestOffice(unittest.TestCase):
	
	def setUp(self):
		self.office = Office()

	def test_office_is_not_full(self):
		result = self.office.isFull()
		self.assertEqual(result,False)	 

	def test_office_is_full(self):
		self.office.current_members = ["marvin","james","kang","andrew","austin","paul","kim"]
		result = self.office.isFull()
		self.assertEqual(result,True)	

if __name__ == '__main__':
    unittest.main()		