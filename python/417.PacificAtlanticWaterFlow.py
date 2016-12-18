def dfs(matrix, ocean, rows, cols, row, col):
	for r, c in ((row+1, col), (row-1, col), (row, col+1), (row,col-1)):
		if r<0 or r>=rows or c>=cols or c<0 or matrix[row][col]>matrix[r][c] or ocean[r][c]==True: continue
		ocean[r][c] = True
		dfs(matrix, ocean, rows, cols, r, c)

class Solution(object):
	def pacificAtlantic(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		if matrix is None or len(matrix)==0 or len(matrix[0])==0: return []
		rows = len(matrix)
		cols = len(matrix[0])
		pacific = [[False]*cols for _ in range(rows)]
		atlantic = [[False]*cols for _ in range(rows)]
		pacific[0] = [True]*cols
		atlantic[-1] = [True]*cols
		for row in range(rows):
			pacific[row][0] = True
			atlantic[row][-1] = True
		for row in range(0,rows):
			dfs(matrix, pacific, rows, cols, row, 0)
			dfs(matrix, atlantic, rows, cols, row, cols-1)
		for col in range(cols):
			dfs(matrix, pacific, rows, cols, 0, col)
			dfs(matrix, atlantic, rows, cols, rows-1, col)
		results = []
		for row in range(rows):
			for col in range(cols):
				if pacific[row][col] and atlantic[row][col]: results.append([row,col])
		return results