from app.storage import Storage


class Fellow(object):
	"""docstring for Fellow"""
	def __init__(self,id_no=0):
		self.id_no = id_no

	"""A  fellow can be allocated either a living space or an office."""	
	"""
	Check if the person of id number X has been allocated room
	
	"""	
	def is_allocated(self,id_no = 0):
		self.id_no = id_no
		if Storage.people_info.has_key(self.id_no):
			return True
		else:
			return False	
