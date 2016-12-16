class MovingAverage(object):

	def __init__(self, size):
		"""
		Initialize your data structure here.
		:type size: int
		"""
		self.size = float(size)
		self.currentSize = 0
		self.avg = 0
		self.queue= []
		

	def next(self, val):
		"""
		:type val: int
		:rtype: float
		"""
		self.queue.append(val)
		if self.currentSize == 0:
			self.avg = val
			self.currentSize = 1
			return val
		elif self.currentSize < self.size:
			self.avg = float((self.avg*self.currentSize + val)) / (self.currentSize+1)
			self.currentSize += 1
			return self.avg
		else:
			remove = self.queue.pop(0)
			self.avg = self.avg + (val-remove)/ self.size
			return self.avg
		
		


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)