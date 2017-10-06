class StringIterator(object):

	def __init__(self, compressedString):
		"""
		:type compressedString: str
		"""
		self.i = 0
		self.s = compressedString
		self.count = 0
		self.c = None

	def next(self):
		"""
		:rtype: str
		"""
		if self.count > 0:
			self.count -= 1
			return self.c
		elif self.i < len(self.s):
			self.c = self.s[self.i]
			j = self.i + 1
			while j < len(self.s) and self.s[j].isdigit():
				j += 1
			self.count = int(self.s[self.i+1:j])-1
			self.i = j
			return self.c
		else:
			return ' '

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.count > 0 or self.i < len(self.s)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()