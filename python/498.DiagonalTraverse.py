class Solution(object):
	def findDiagonalOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix or not matrix[0]: return []
		m, n = len(matrix), len(matrix and matrix[0])
		return [matrix[i][d-i]
			for d in range(m+n-1)
			for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]