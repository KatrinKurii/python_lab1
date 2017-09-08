class Book(object):
	def __init__(self, aid, bid, bname):
		self.aid = aid;
		self.bid = bid
		self.bname = bname
	def __str__(self):
		return "aid=%d, bid=%d, bname = %s" % (self.aid, self.bid, self.bname)
book1 = Book(1, 2, 'A1')
print book1
	
	
	