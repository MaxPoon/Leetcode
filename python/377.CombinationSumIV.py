class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if target <= 0 : return 0
		dp = [0]*(target+1)
		dp[0] = 1
		for i in range(target+1):
			for num in nums:
				if i - num >= 0:
					dp[i] += dp[i-num]
		return dp[-1]
