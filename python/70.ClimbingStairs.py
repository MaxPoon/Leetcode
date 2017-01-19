class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		sqrt5 = 5**0.5
		return int(round((((1+sqrt5)/2)**(n+1) - ((sqrt5-1)/2)**(n+1))/sqrt5))