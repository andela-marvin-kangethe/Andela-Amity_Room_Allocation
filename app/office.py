
class Office(object):
	"""docstring for Office"""
	

	def __init__(self,name = ""):
		self.name = name
		self.current_members = []
		self.maximum_capacity = 6
		
	"""
	Check if the length of list of current occupants is greater than the room limit
	"""	
	def isFull(self):
		if len(self.current_members) < self.maximum_capacity:
			return False
		else:
			return True	
