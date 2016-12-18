class Solution(object):
	def minAbbreviation(self, target, dictionary):
		"""
		:type target: str
		:type dictionary: List[str]
		:rtype: str
		"""
		self.target = target
		self.size = len(target)
		self.dlist = [d for d in dictionary if len(d) == self.size]
		self.ans = target
		self.length = self.size
		self.dfs('', 0, 0)
		return self.ans
	def dfs(self, abbr, length, depth):
		if length >= self.length: return
		if depth == self.size:
			for word in self.dlist:
				if self.validWordAbbreviation(word, abbr):
					return
			self.ans = abbr
			self.length = length
			return
		if depth == 0 or not abbr[-1].isdigit():
			for x in range( self.size - depth, 1, -1):
				self.dfs(abbr + str(x), length + 1, depth + x)
		self.dfs(abbr + self.target[depth], length + 1, depth + 1)
	def validWordAbbreviation(self, word, abbr):
		"""
		:type word: str
		:type abbr: str
		:rtype: bool
		"""
		size = len(word)
		cnt = loc = 0
		for w in abbr:
			if w.isdigit():
				if w == '0' and cnt == 0:
					return False
				cnt = cnt * 10 + int(w)
			else:
				loc += cnt
				cnt = 0
				if loc >= size or word[loc] != w:
					return False
				loc += 1
		return loc + cnt == size