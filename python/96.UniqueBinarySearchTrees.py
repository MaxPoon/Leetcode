class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0: return 0
		dp = [1]*(n+1)
		for i in range(2, n+1):
			total = 0
			for root in range(1, i+1):
				total += dp[root-1]*dp[i-root]
			dp[i] = total
		return dp[-1]
