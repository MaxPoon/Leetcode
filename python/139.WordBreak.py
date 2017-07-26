class TrieNode:
	def __init__(self, char):
		self.char = char
		self.children = {}
		self.isEnd = False
	def __hash__(self):
		return id(self)
	def __eq__(self, other):
		return id(self)==id(other)

class Trie:
	def __init__(self):
		self.root = TrieNode(None)
	def addWord(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				newNode = TrieNode(c)
				node.children[c] = newNode
			node = node.children[c]
		node.isEnd = True

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		trie = Trie()
		for word in wordDict:
			trie.addWord(word)
		root = trie.root
		trieNodeSet = set([root])
		for c in s:
			newTrieNodeSet = set()
			for node in trieNodeSet:
				if c in node.children:
					if node.children[c].isEnd:
						newTrieNodeSet.add(root)
					newTrieNodeSet.add(node.children[c])
			if not newTrieNodeSet:
				return False
			trieNodeSet = newTrieNodeSet
		for node in trieNodeSet:
			if node.isEnd:
				return True
		return False
