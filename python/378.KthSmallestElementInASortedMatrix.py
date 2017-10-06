class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		n = len(matrix)
		L, R = matrix[0][0], matrix[n - 1][n - 1]
		while L < R:
			mid = L + ((R - L) >> 1)
			temp = self.search_lower_than_mid(matrix, n, mid)
			if temp < k:
				L = mid + 1
			else:
				R = mid
		return L
 
	def search_lower_than_mid(self, matrix, n, x):
		i, j = n - 1, 0
		cnt = 0
		while i >= 0 and j < n:
			if matrix[i][j] <= x:
				j += 1
				cnt += i + 1
			else:
				i -= 1
		return cnt
