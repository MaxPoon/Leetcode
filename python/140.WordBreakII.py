class TrieNode:
	def __init__(self, char):
		self.char = char
		self.children = {}
		self.isEnd = False
		self.words = set()
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
		node.words.add(word)

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		trie = Trie()
		for word in wordDict:
			trie.addWord(word)
		root = trie.root
		trieNodeSet = set([root])
		endWords = [set() for i in range(len(s))]
		for i, c in enumerate(s):
			newTrieNodeSet = set()
			for node in trieNodeSet:
				if c in node.children:
					if node.children[c].isEnd:
						newTrieNodeSet.add(root)
						endWords[i].update(node.children[c].words)
					newTrieNodeSet.add(node.children[c])
			if not newTrieNodeSet:
				return []
			trieNodeSet = newTrieNodeSet
		paths = []
		def findPaths(i, paths, currentPath):
			for word in endWords[i]:
				if i+1-len(word) == 0:
					paths.append(currentPath + [word])
				else:
					currentPath.append(word)
					findPaths(i-len(word), paths, currentPath)
					currentPath.pop()
		findPaths(len(s)-1, paths, [])
		return [" ".join(path[::-1]) for path in paths]
