class Solution(object):
	def isStrobogrammatic(self, num):
		"""
		:type num: str
		:rtype: bool
		"""
		rotate ={"0":"0", "1":"1", "6":"9", "8":"8", "9": "6"}
		for i,n in enumerate(num):
			if n not in rotate: return False
			if rotate[n] != num[len(num)-1-i]: return False
			if i>=(len(num)-1)/2: return True