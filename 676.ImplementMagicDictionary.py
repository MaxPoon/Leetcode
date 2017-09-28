from string import ascii_lowercase
class MagicDictionary(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.dict = set()
		

	def buildDict(self, dict):
		"""
		Build a dictionary through a list of words
		:type dict: List[str]
		:rtype: void
		"""
		self.dict = set()
		for word in dict:
			for i, c in enumerate(word):
				for c2 in ascii_lowercase:
					if c == c2: continue
					newWord = word[:i] + c2 + word[i+1:]
					self.dict.add(newWord)

	def search(self, word):
		"""
		Returns if there is any word in the trie that equals to the given word after modifying exactly one character
		:type word: str
		:rtype: bool
		"""
		return word in self.dict


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)