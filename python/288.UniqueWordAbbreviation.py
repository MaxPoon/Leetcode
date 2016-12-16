class ValidWordAbbr(object):
	def __init__(self, dictionary):
		"""
		initialize your data structure here.
		:type dictionary: List[str]
		"""
		self.dictionary = set(dictionary)
		self.count = {}
		for word in self.dictionary:
			if len(word)>=3:
				abbr = word[0] + str(len(word)-1) + word[-1]
			else: abbr = word
			if abbr not in self.count:self.count[abbr] = 1
			else: self.count[abbr] = 2
		

	def isUnique(self, word):
		"""
		check if a word is unique.
		:type word: str
		:rtype: bool
		"""
		if len(word)>=3:
			abbr = word[0] + str(len(word)-1) + word[-1]
		else: abbr = word
		if word not in self.dictionary and abbr in self.count:return False
		if abbr in self.count and self.count[abbr] ==2: return False
		return True


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")