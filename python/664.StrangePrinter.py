class Solution(object):
	def strangePrinter(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		memo = {}
		def dp(i, j):
			if i > j: return 0
			if (i, j) not in memo:
				ans = dp(i+1, j) + 1
				for k in xrange(i+1, j+1):
					if s[k] == s[i]:
						ans = min(ans, dp(i, k-1) + dp(k+1, j))
				memo[i, j] = ans
			return memo[i, j]

		return dp(0, len(s) - 1)
