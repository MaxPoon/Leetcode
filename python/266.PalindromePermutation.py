class Solution(object):
	def canPermutePalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		letterCount = {}
		for c in s:
			letterCount[c] = letterCount.get(c, 0) + 1
		odd = 0
		for count in letterCount.values():
			if count&1:
				odd += 1
				if odd == 2 or (odd == 1 and len(s)&1==0):
					return False
		return True
