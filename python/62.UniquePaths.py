class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		dp = [1]*n
		for _ in range(1, m):
			for i in range(1, n):
				dp[i] = dp[i-1] + dp[i]
		return dp[-1]
