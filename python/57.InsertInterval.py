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
        if len(intervals)==0:
            return [newInterval]
        result = []
        for interval in intervals:
            if newInterval.start>interval.end or newInterval.end<interval.start:
                result.append(interval)
            else:
                newInterval.start = min(newInterval.start,interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        result.append(newInterval)
        result=sorted(result, key = lambda x:x.start)
        return result
