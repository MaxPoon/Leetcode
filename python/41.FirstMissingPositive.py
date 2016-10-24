class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums)==0:
			return 1
		if len(nums)==1:
			return 2 if nums[0]==1 else 1
		for i in range(len(nums)):
			while nums[i]>0 and nums[i]<=len(nums) and nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
				nums[nums[i]-1], nums[i]=nums[i], nums[nums[i]-1]
		for i, n in enumerate(nums):
			if n!=i+1:
				return i+1
		return len(nums)+1