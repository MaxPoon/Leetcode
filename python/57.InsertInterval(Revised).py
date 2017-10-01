# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		"""
		if not intervals:
			return [newInterval]
		if newInterval.start > intervals[-1].end:
			intervals.append(newInterval)
			return intervals
		if newInterval.end < intervals[0].start:
			return [newInterval] + intervals
		newIntervals = []
		mergeStart = None
		for i, interval in enumerate(intervals[:-1]):
			nextInterval = intervals[i+1]
			if interval.end < newInterval.start and nextInterval.start > newInterval.end:
				return intervals[:i+1] + [newInterval] + intervals[i+1:]
		for i, interval in enumerate(intervals):
			if (interval.start <= newInterval.end and newInterval.start <= interval.start) or (newInterval.end >= interval.end and newInterval.start <= interval.end):
				mergeStart = i
				break
		if mergeStart is None:
			return intervals
		mergeEnd = mergeStart
		for j in range(i+1, len(intervals)):
			interval = intervals[j]
			if newInterval.end >= interval.start:
				mergeEnd = j
			if newInterval.end <= interval.end:
				break
		start = min(intervals[mergeStart].start, newInterval.start)
		end = max(intervals[mergeEnd].end, newInterval.end)
		mergedInterval = Interval(start, end)
		return intervals[:mergeStart] + [mergedInterval] + intervals[mergeEnd+1:]
