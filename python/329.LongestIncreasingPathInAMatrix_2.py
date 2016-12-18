class Solution(object):
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		if matrix is None or len(matrix)==0 or len(matrix[0])==0: return 0
		points = []
		rows = len(matrix)
		cols = len(matrix[0])
		longest = [[0]*cols for _ in range(rows)]
		for row in range(rows):
			for col in range(cols):
				points.append((matrix[row][col], row, col))
		points.sort(reverse=True)
		i = 0
		maxLength = 0
		while i<len(points):
			val, row, col = points[i]
			length = 1
			for r,c in ((row+1, col), (row-1,col), (row,col+1),(row,col-1)):
				if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c]<=matrix[row][col]: continue
				length = max(length, longest[r][c]+1)
			longest[row][col] = length
			maxLength = max(maxLength, length)
			i += 1
		return maxLength