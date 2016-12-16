class ZigzagIterator(object):

	def __init__(self, v1, v2):
		"""
		Initialize your data structure here.
		:type v1: List[int]
		:type v2: List[int]
		"""
		self.l = []
		p1, p2 = 0, 0
		isOne = True
		while p1<len(v1) and p2 < len(v2):
			if isOne:
				self.l.append(v1[p1])
				p1 += 1
			else:
				self.l.append(v2[p2])
				p2 += 1
			isOne = not isOne
		if p1<len(v1):
			self.l += v1[p1:]
		if p2<len(v2):
			self.l += v2[p2:]
		self.p = 0

	def next(self):
		"""
		:rtype: int
		"""
		self.p += 1
		return self.l[self.p-1]

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.p<len(self.l)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())