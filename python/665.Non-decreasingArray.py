class Solution(object):
	def checkPossibility(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		count = 0
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				if count == 0:
					if i == 0 or nums[i-1] <= nums[i+1]:
						nums[i] = nums[i-1]
					else:
						nums[i+1] = nums[i]
					count = 1
				else: return False
		return True
