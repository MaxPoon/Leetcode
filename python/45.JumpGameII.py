class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) <= 1: return 0
		jumps, curEnd, curFarthest = 1, 0, 0
		for i in range(len(nums)):
			curFarthest = max(curFarthest, i + nums[i])
			if curFarthest >= len(nums)-1: return jumps
			if i == curEnd:
				jumps += 1
				curEnd = curFarthest
