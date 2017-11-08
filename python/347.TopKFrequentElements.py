from collections import Counter
from heapq import heappush, heappushpop
class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		c = Counter(nums)
		heap = []
		for num, count in c.items():
			if len(heap) < k:
				heappush(heap, (count, num))
			elif count > heap[0][0]:
				heappushpop(heap, (count, num))
		return [num for count, num in heap]
