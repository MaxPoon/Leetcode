class PhoneDirectory(object):

	def __init__(self, maxNumbers):
		"""
		Initialize your data structure here
		@param maxNumbers - The maximum numbers that can be stored in the phone directory.
		:type maxNumbers: int
		"""
		self.released = set()
		self.current = -1
		self.max = maxNumbers

	def get(self):
		"""
		Provide a number which is not assigned to anyone.
		@return - Return an available number. Return -1 if none is available.
		:rtype: int
		"""
		if self.released:
			return self.released.pop()
		if self.current + 1 >= self.max: return -1
		self.current += 1
		return self.current

	def check(self, number):
		"""
		Check if a number is available or not.
		:type number: int
		:rtype: bool
		"""
		return number > self.current or number in self.released

	def release(self, number):
		"""
		Recycle or release a number.
		:type number: int
		:rtype: void
		"""
		if number <= self.current:
			self.released.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)