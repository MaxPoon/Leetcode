from heapq import heappush, heappop, heapify
from collections import defaultdict
class Solution(object):
	def medianSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[float]
		"""
		if k==1: return [float(num) for num in nums]
		invalid = defaultdict(int)
		maxHeap = []
		minHeap = nums[:k]
		heapify(minHeap)
		for i in range(k//2):
			heappush(maxHeap, -heappop(minHeap))
		invalidInMax = 0
		invalidInMin = 0
		medians = [float(minHeap[0]) if k&1 else (minHeap[0]-maxHeap[0])/2.0]
		diff = 1 if k&1 else 0
		for i in range(k, len(nums)):
			inNum = nums[i]
			outNum = nums[i-k]
			if outNum >= minHeap[0]:
				invalidInMin += 1
			else:
				invalidInMax += 1
			invalid[outNum] += 1
			if inNum >= minHeap[0]:
				heappush(minHeap, inNum)
			else:
				heappush(maxHeap, -inNum)
			while (len(minHeap)-invalidInMin) - (len(maxHeap)-invalidInMax) < diff:
				heappush(minHeap, -heappop(maxHeap))
			while (len(minHeap)-invalidInMin) - (len(maxHeap)-invalidInMax) > diff:
				heappush(maxHeap, -heappop(minHeap))
			while invalid[minHeap[0]]:
				invalid[minHeap[0]] -= 1
				heappop(minHeap)
				invalidInMin -= 1
			while invalid[-maxHeap[0]]:
				invalid[-maxHeap[0]] -= 1
				heappop(maxHeap)
				invalidInMax -= 1
			medians.append(float(minHeap[0]) if k&1 else (minHeap[0]-maxHeap[0])/2.0)
		return medians
