class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums)==1: return 0
		if nums[0] > nums[1]: return 0
		if nums[-1] > nums[-2]: return len(nums)-1
		left = 0
		right = len(nums) - 1
		while left<right:
			mid = (left+right)//2
			if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]: return mid
			if nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1]: left = mid
			else: right = mid
		return right