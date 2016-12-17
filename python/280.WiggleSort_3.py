class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if len(nums)<2: return
		i = 0
		while i<len(nums)-1:
			if (i&1==0 and nums[i]>nums[i+1]) or (i&1==1 and nums[i]<nums[i+1]):
				nums[i], nums[i+1] = nums[i+1], nums[i]
			i+=1