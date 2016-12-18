class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		squares = []
		for i in range(1,int(n**0.5+1)):
			squares.append(i**2)
		dp = [0] * (n+1)
		for i in range(1,n+1):
			m = i
			for square in squares:
				if i-square<0: break
				if m>dp[i-square]: m = dp[i-square]
			dp[i] = m+1
		return dp[n]