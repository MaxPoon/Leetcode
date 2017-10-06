from math import ceil
class Solution(object):
	def repeatedStringMatch(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: int
		"""
		n = int(ceil(float(len(B))/len(A)))
		s = A*(n+1)
		i = s.find(B)
		if i + len(B) > len(A)*n:
			return n+1
		elif i >= 0:
			return n
		else:
			return -1
