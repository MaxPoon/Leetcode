class Solution(object):
	def constructArray(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[int]
		"""
		ans = list(range(1, n-k))
		for i in range(k+1):
			if i % 2 == 0:
				ans.append(n-k+i/2)
			else:
				ans.append(n-i//2)
		return ans
