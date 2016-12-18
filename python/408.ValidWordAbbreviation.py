class Solution(object):
	def validWordAbbreviation(self, word, abbr):
		"""
		:type word: str
		:type abbr: str
		:rtype: bool
		"""
		p1 = 0
		p2 = 0
		while p1<len(word) and p2<len(abbr):
			if abbr[p2].isdigit():
				if int(abbr[p2])==0: return False
				i = 0
				while p2+i<len(abbr) and abbr[p2+i].isdigit():
					i+=1
				n = int(abbr[p2:p2+i])
				if len(word)-p1<n: return False
				else: 
					p1+=n
					p2+=i
			else:
				if abbr[p2]!=word[p1]: return False
				else:
					p1+=1
					p2+=1
		if p1!=len(word) or p2!=len(abbr): return False
		return True