class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = list(set(nums))
		if len(nums)==0: return 0
		if len(nums)==1: return 1
		nums.sort()
		current = 1
		longest = 1
		for i in range(1,len(nums)):
			if nums[i] - nums[i-1]==1:
				current+=1
				longest = max(longest,current)
			else:
				current = 1
		return longest