class Solution(object):
	def generatePossibleNextMoves(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		if len(s)<2: return []
		moves = []
		for i in range(1,len(s)):
			if s[i-1:i+1] == "++":
				moves.append(s[:i-1] + "--" + s[i+1:])
		return moves