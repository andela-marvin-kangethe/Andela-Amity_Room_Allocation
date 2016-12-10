from app.livingspace import LivingSpace
import unittest  


class Test(unittest.TestCase):
	
	def setUp(self):
		self.livingspace = LivingSpace()

	def test_livingspace_is_not_full(self):
		result = self.livingspace.isFull()
		self.assertEqual(result,False, msg = "The livingspace is now full")	 