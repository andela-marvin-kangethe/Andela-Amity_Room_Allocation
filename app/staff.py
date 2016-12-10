from app.storage import Storage


class Staff(object):
    """docstring for Staff"""

    def __init__(self, id_no=0):
        self.id_no = id_no

    """
	Check if the person with id no X has been allocated room
	"""

    def is_allocated(self, id_no=0):
        self.id_no = id_no
        if Storage.people_info.has_key(self.id_no):
			return True
		# else:
		# 	return False
