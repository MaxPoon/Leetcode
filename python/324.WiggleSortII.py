class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		temp = sorted(nums)
		p1, p2 = (len(nums) + 1) >> 1, len(nums)
		for i in range(len(nums)):
			if i & 1 == 0:
				p1 -= 1
				nums[i] = temp[p1]
			else:
				p2 -= 1
				nums[i] = temp[p2]