class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = 0
		maxCount = 0
		lastFlip = -1
		for i, num in enumerate(nums):
			if num == 1:
				count += 1
			else:
				count = i - lastFlip
				lastFlip = i
			maxCount = max(count, maxCount)
		return maxCount
