class Solution(object):
	def findTheDifference(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		hashS = {}
		hashT = {}
		for c in s:
			if c not in hashS: hashS[c]=1
			else: hashS[c]+=1
		for c in t:
			if c not in hashT: hashT[c]=1
			else: hashT[c]+=1
		for c, v in hashT.items():
			if c not in hashS or hashS[c]!=v: return c