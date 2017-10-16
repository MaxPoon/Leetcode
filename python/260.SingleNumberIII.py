class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = set()
		for num in nums:
			if num in result:
				result.remove(num)
			else:
				result.add(num)
		return list(result)
