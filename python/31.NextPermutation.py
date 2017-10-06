class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if len(nums) <= 1: return
		for i in range(len(nums)-2, -1, -1):
			if nums[i] >= nums[i+1]:
				continue
			j = len(nums)-1
			while True:
				if nums[j] > nums[i]: break
				j -= 1
			nums[i], nums[j] = nums[j], nums[i]
			nums[i+1:] = list(reversed(nums[i+1:]))
			return
		nums.reverse()
