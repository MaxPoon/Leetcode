class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		m = len(matrix)
		if m == 0: return False
		n = len(matrix[0])
		if n == 0: return False
		r, c = 0, n-1
		while r < m and c >= 0:
			if matrix[r][c] == target:
				return True
			if matrix[r][c] > target:
				c -= 1
			else: 
				r += 1
		return False
