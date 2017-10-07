class Solution(object):
	def findMaxForm(self, strs, m, n):
		"""
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""
		counts = [None]*len(strs)
		for i, string in enumerate(strs):
			zeros = 0
			for c in string:
				if c == '0': zeros+=1
			counts[i] = (zeros, len(string)-zeros)
		dp = [[0]*(n+1) for _ in range(m+1)]
		for zeros, ones in counts:
			for i in range(m, zeros-1, -1):
				for j in range(n, ones-1, -1):
					dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
		return dp[-1][-1]
