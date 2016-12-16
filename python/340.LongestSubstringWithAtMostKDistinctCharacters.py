class Solution(object):
	def lengthOfLongestSubstringKDistinct(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""
		if len(s)==0 or k==0: return 0
		p1, p2 = 0, 0
		d = {}
		distinc = 0
		longest = 0
		while p2<len(s):
			c = s[p2]
			if c not in d or d[c] < p1:
				distinc += 1
			d[c] = p2
			if distinc > k:
				longest = max(longest, p2-p1)
				while p1 != d[s[p1]]: p1+=1
				p1+=1
				distinc-=1
			p2 += 1
		longest = max(longest, p2-p1)
		return longest