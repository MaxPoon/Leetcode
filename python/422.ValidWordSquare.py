class Solution(object):
	def validWordSquare(self, words):
		"""
		:type words: List[str]
		:rtype: bool
		"""
		m = len(words)
		n = len(words[0]) if m else 0
		if m != n:
			return False
		for x in range(m):
			n = len(words[x])
			c = 0
			for y in range(m):
				if len(words[y]) < x + 1:
					break
				c += 1
			if c != n:
				return False
			for y in range(n):
				if words[x][y] != words[y][x]:
					return False
		return True