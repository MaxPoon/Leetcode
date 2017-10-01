class Vector2D(object):

	def __init__(self, vec2d):
		"""
		Initialize your data structure here.
		:type vec2d: List[List[int]]
		"""
		self.row = 0
		self.col = -1
		self.matrix = vec2d

	def next(self):
		"""
		:rtype: int
		"""
		if self.hasNext():
			self.col += 1
			return self.matrix[self.row][self.col]
		else:
			return None
		

	def hasNext(self):
		"""
		:rtype: bool
		"""
		if self.row >= len(self.matrix): return False
		if self.col >= len(self.matrix[self.row])-1:
			self.row += 1
			while self.row < len(self.matrix):
				if self.matrix[self.row]:
					self.col = -1
					return True
				self.row += 1
			return False
		else:
			return True
		

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())