class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums.sort()
		if len(nums)<3: return
		i = 2
		while i<len(nums):
			nums[i],nums[i-1] = nums[i-1],nums[i]
			i+=2