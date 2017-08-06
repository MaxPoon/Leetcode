class Solution(object):
	def numberOfArithmeticSlices(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		n = len(A)
		dp, locs, res = [[0]*n for _ in range(n)], {}, 0
		for i, num in enumerate(A):
			locs[num] = locs.get(num, []) + [i]
		for j in range(n-2,0,-1):
			for i in range(j-1,-1,-1):
				target = 2*A[j] - A[i]
				for k in locs.get(target, []):
					if k > j:
						dp[i][j] += dp[j][k] + 1
				res += dp[i][j]
		return res
