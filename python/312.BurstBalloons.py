class Solution(object):
	def maxCoins(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = [1] + nums + [1]
		dp = [[None]*len(nums) for _ in nums]
		return self.getMaxCoinsBetween(0, len(nums)-1, dp, nums)
		
	def getMaxCoinsBetween(self, i, j, dp, nums):
		if dp[i][j] != None:
			return dp[i][j]
		maxCoins = 0
		for k in range(i+1, j):
			coins = nums[k]
			if i != -1:
				coins *= nums[i]
			if j != len(nums):
				coins *= nums[j]
			if i != -1:
				coins += self.getMaxCoinsBetween(i, k, dp, nums)
			if j != len(nums):
				coins += self.getMaxCoinsBetween(k, j, dp, nums)
			maxCoins = max(maxCoins, coins)
		dp[i][j] = maxCoins
		return maxCoins
