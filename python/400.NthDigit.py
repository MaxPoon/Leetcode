class Solution(object):
	def findNthDigit(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n<10: return n
		i = 1
		while n>9*(10**(i-1))*i:
			n -= 9*(10**(i-1))*i
			i += 1
		x = (n-1)//i
		x = 10**(i-1) + x
		m = (n-1)%i
		return int(str(x)[m])