from heapq import heappush, heappop
class Solution(object):
	def kSmallestPairs(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[List[int]]
		"""
		i = 0
		heap = []
		stop = k
		while i < len(nums1) and i < k:
			j = 0
			while j < len(nums2) and j < stop:
				if len(heap) < k or nums1[i]+nums2[j] < -heap[0][0]:
					if len(heap) == k:
						heappop(heap)
					heappush(heap, (-nums1[i]-nums2[j], nums1[i], nums2[j]))
					j += 1
				else:
					stop = j
					break
			i += 1
		result = [(pair[1], pair[2]) for pair in heap]
		return result
