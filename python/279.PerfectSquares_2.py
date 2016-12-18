class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if int(n**0.5)**2 == n: return 1
		while n%4==0: n/=4
		if n%8 == 7: return 4
		for a in range(int(n**0.5),0,-1):
			b = int((n-a*a)**0.5)
			if a*a+b*b==n:
				return 2
		return 3