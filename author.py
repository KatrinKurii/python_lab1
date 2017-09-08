class Author(object):
	def __init__(self, aid, aname):
		self.aid = aid;
		self.aname = aname
	def __str__(self):
		return "aid=%d, aname = %s" % (self.aid, self.aname)
author1 = Author(1, 'A1')
print author1
	