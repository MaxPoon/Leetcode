class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		if digits is None or len(digits)==0: return None
		c = 1
		for i in range(len(digits) -1, -1, -1):
			s = digits[i]+c
			c = s//10
			digits[i] = s%10
		if c:
			digits = [1] + digits
		return digits