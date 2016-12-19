# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *
class Solution(object):
	def minMeetingRooms(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		if len(intervals)==0: return 0
		intervals.sort(key= lambda x: x.start)
		heap = []
		required = 1
		for interval in intervals:
			while len(heap) and interval.start >= heap[0]:
				heappop(heap)
			heappush(heap, interval.end)
			required = max(required, len(heap))
		return required