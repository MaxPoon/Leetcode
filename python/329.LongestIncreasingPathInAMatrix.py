def dfs(matrix, longest, rows, cols, row, col):
	if longest[row][col]!=0: return
	longest[row][col] = 1
	for (r,c) in ((row+1, col), (row-1,col), (row,col+1),(row,col-1)):
		if r<0 or r>=rows or c<0 or c>=cols or matrix[row][col]>=matrix[r][c]: continue
		if longest[r][c] == 0: dfs(matrix, longest, rows, cols, r, c)
		longest[row][col] = max(longest[row][col], longest[r][c]+1)

class Solution(object):
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		if matrix is None or len(matrix)==0 or len(matrix[0])==0: return 0
		rows = len(matrix)
		cols = len(matrix[0])
		longest = [[0]*cols for _ in range(rows)]
		for row in range(rows):
			for col in range(cols):
				dfs(matrix, longest, rows, cols, row, col)
		length = 0
		for row in range(rows):
			length = max(length, max(longest[row]))
		return length