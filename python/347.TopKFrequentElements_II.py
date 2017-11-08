from collections import Counter
class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		c = Counter(nums)
		bucket = [[] for i in range(len(nums)+1)]
		for num, count in c.items():
			bucket[count].append(num)
		result = []
		for i in range(len(nums), 0, -1):
			for num in bucket[i]:
				result.append(num)
				if len(result) == k:
					return result
