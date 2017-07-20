class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
		dp[0][0] = True
		# dp[i][j] == True means s[:i] matches p[:j]
		for i in range(len(s)+1):
			for j in range(1, len(p)+1):
				if p[j-1] == '*':
					dp[i][j] = (dp[i][j-2]) or (i > 0 and (p[j-2] == '.' or p[j-2] == s[i-1]) and dp[i-1][j])
				else:
					dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
		return dp[-1][-1]