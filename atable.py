from author import Author
class Authors (object):
	def __init__ (self):
		self.authors = []
	def add(self, author):
		self.authors.append(author)
	def __str__ (self):
		for author in self.authors:
			return '\n'.join(str(author) for author in self.authors)
authors = Authors()
author1 = Author(1, 'as')
authors.add(author1)
author1 = Author(2, 'vc')
authors.add(author1)
print authors