class Solution(object):
	def findMaxAverage(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: float
		"""
		s = sum(nums[:k])
		maxSum = s
		for i in range(k, len(nums)):
			s -= nums[i-k]
			s += nums[i]
			maxSum = max(s, maxSum)
		return maxSum/float(k)
