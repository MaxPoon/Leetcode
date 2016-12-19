class Solution(object):
	def numWays(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: int
		"""
		if n==0: return 0
		if n==1: return k
		if n==2: return k*k
		dp = [[0,0] for i in xrange(n)]
		dp[1][0] = k*(k-1)
		dp[1][1] = k
		for i in xrange(2,n):
			dp[i][0] = (dp[i-1][0] + dp[i-1][1])*(k-1)
			dp[i][1] = dp[i-1][0]
		return sum(dp[-1])