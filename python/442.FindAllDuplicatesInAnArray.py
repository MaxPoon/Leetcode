class Solution(object):
	def findDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		for i in range(len(nums)):
			while nums[i] !=i+1:
				if nums[nums[i]-1]==nums[i]:
					break
				else:
					nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
		result = []
		for i, n in enumerate(nums):
			if i+1!=n:
				result.append(nums[i])
		return result