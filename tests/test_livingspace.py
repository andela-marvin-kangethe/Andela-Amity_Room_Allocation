from app.livingspace import LivingSpace
import unittest  


class TestLivingspace(unittest.TestCase):
	
	def setUp(self):
		self.livingspace = LivingSpace()

	def test_livingspace_is_not_full(self):
		result = self.livingspace.isFull()
		self.assertEqual(result,False)	 

	def test_livingspace_is_full(self):
		self.livingspace.current_members = ["marvin","james","kang","andrew","austin"]
		result = self.livingspace.isFull()
		self.assertEqual(result,True)	

if __name__ == '__main__':
    unittest.main()		