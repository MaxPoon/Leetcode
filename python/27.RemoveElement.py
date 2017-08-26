class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		length = 0
		for i in xrange(len(nums)):
			num = nums[i]
			if num != val:
				nums[length] = num
				length += 1
		return length
