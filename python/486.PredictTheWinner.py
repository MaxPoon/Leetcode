class Solution(object):
	def PredictTheWinner(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		cache = {}
		def maximize(nums, i, j):
			if i == j:
				return nums[i]
			if (i, j) in cache:
				return cache[(i, j)]
			cache[(i, j)] = max(nums[i]-maximize(nums, i+1, j), nums[j]-maximize(nums, i, j-1))
			return cache[(i, j)]
		return maximize(nums, 0, len(nums)-1) >= 0
