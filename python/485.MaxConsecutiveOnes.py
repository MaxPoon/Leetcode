class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = 0
		maxCount = 0
		for num in nums:
			if num == 1:
				count += 1
				maxCount = max(count, maxCount)
			else:
				count = 0
		return maxCount
