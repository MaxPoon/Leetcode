class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		count = {}
		for c in s:
			count[c] = count.get(c, 0) + 1
		hasOdd = False
		length = 0
		for v in count.values():
			length += v
			if v&1==1:
				hasOdd = True
				length -= 1
		if hasOdd:
			length += 1
		return length