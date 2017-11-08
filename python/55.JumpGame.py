class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		lastIndex = len(nums)-1
		for i in range(len(nums)-2, -1, -1):
			if nums[i]+i >= lastIndex: lastIndex = i
		return lastIndex == 0
