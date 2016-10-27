from math import ceil 
class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x<0:return False
		x=str(x)
		for i in range(int(ceil(len(x)/2))):
			if x[i]!=x[len(x)-i-1]:return False
		return True