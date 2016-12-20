class Solution(object):
	def maxProduct(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		if len(words)<2: return 0
		hashTable = [0]*len(words)
		for j,word in enumerate(words):
			hashed = 0
			for letter in word:
				i = ord(letter) - 97
				hashed |= 1<<i
			hashTable[j] = hashed
		maximum = 0
		for i in xrange(len(words)-1):
			for j in xrange(i+1, len(words)):
				if hashTable[i] & hashTable[j] == 0:
					maximum = max(maximum, len(words[i])*len(words[j]))
		return maximum