class Solution(object):
	def findContestMatch(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		matches = [str(i) for i in range(1, n+1)]
		while n > 1:
			half = n/2
			for i in range(half):
				matches[i] = '(' + matches[i] + ',' + matches[n-i-1] + ')'
			n = half
		return matches[0]
