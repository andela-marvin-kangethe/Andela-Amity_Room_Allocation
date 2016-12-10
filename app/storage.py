


class Storage(object):

	total_no_of_rooms = 0
						
	list_of_unallocated_people = []			
	list_of_all_rooms =[]
	list_of_all_people =[]	
	people_info = {}

	unallocated_people_info = {}
	"""
	total_no_of_rooms 					increment by 4 if room is living and 6 if room is office					
	list_of_unallocated_people = []		store people instance for the ones without rooms but want allocation.
	list_of_all_rooms =[]				store all room instances.
	people_info = {}					store the name of person as value and id number as key.
	"""

	def __init__(self):
		pass
		
