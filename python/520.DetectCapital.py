class Solution(object):
	def detectCapitalUse(self, word):
		"""
		:type word: str
		:rtype: bool
		"""
		return word == word.upper() or word[1:] == word[1:].lower()
