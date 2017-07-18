from heapq import *
class Solution:
	def smallestRange(self, nums):
		"""
		:type nums: List[List[int]]
		:rtype: List[int]
		"""
		heap = []
		pointers = [0]*len(nums)
		for i, sortedList in enumerate(nums):
			heappush(heap, (sortedList[0], i))
		start = heap[0][0]
		end = max(heap)[0]
		largest = end
		while True:
			value, i = heappop(heap)
			pointers[i] += 1
			if pointers[i] == len(nums[i]):
				break
			value = nums[i][pointers[i]]
			heappush(heap, (value, i))
			largest = max(largest, value)
			if largest - heap[0][0] < end - start:
				start = heap[0][0]
				end = largest
		return [start, end]
