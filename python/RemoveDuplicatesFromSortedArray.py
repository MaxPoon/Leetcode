class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		prev = None
		length = 0
		for i in xrange(len(nums)):
			num = nums[i]
			if num != prev:
				nums[length] = num
				length += 1
				prev = num
		return length
