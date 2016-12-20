class TrieNode(object):
	def __init__(self, char):
		self.char = char
		self.next = {}
		self.end = []

class Trie(object):
	def __init__(self):
		self.root = TrieNode(None)
		
	def add(self, word):
		node = self.root
		for i, c in enumerate(word):
			if c not in node.next:
				node.next[c] = TrieNode(c)
			node = node.next[c]
		node.end.append(word)
		
def dfs(rows, cols, row, col, board, node, visited, found):
	for word in node.end:
		found.add(word)
	for r, c in ((row+1, col), (row-1,col), (row,col+1), (row,col-1)):
		if 0<=r<rows and 0<=c<cols and (r,c) not in visited and board[r][c] in node.next:
			visited.add((r,c))
			dfs(rows, cols, r, c, board, node.next[board[r][c]], visited, found)
			visited.remove((r,c))

class Solution(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		if board is None or len(board)==0 or len(board[0])==0: return []
		rows = len(board)
		cols = len(board[0])
		t = Trie()
		for word in words:
			t.add(word)
		found = set()
		visited = set()
		for row in range(rows):
			for col in range(cols):
				if board[row][col] in t.root.next:
					visited.add((row,col))
					dfs(rows, cols, row, col, board, t.root.next[board[row][col]], visited, found)
					visited.remove((row,col))
		return list(found)