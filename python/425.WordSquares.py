class TrieNode(object):
	def __init__(self):
		self.next = {}
		self.indexes = set()
		

class Trie(object):
	def __init__(self):
		self.root = TrieNode()
	def add(self, word, index):
		currentNode = self.root
		for c in word:
			if c not in currentNode.next: currentNode.next[c] = TrieNode()
			currentNode = currentNode.next[c]
			currentNode.indexes.add(index)
	def getIndexes(self, prefix):
		currentNode = self.root
		for i, c in enumerate(prefix):
			if c not in currentNode.next: return []
			currentNode = currentNode.next[c]
		return list(currentNode.indexes)

def recursive(t, words, added, l, result):
	if len(added)==l:
		newResult = []
		for i in added:
			word = words[i]
			newResult.append(word)
		result.append(newResult)
		return
	i = len(added)
	prefix = ""
	for j in range(i):
		prefix += words[added[j]][i]
	indexes = t.getIndexes(prefix)
	for index in indexes:
		added.append(index)
		recursive(t, words, added, l, result)
		added.pop()

class Solution(object):
	def wordSquares(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[str]]
		"""
		if len(words)==0: return []
		t = Trie()
		for i, word in enumerate(words):
			t.add(word, i)
		for i in range(len(words)): t.root.indexes.add(i)
		added = []
		l = len(words[0])
		result = []
		recursive(t, words, added, l, result)
		return result