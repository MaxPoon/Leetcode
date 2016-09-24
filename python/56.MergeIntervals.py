# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result  =[]
        if len(intervals) == 0:
            return result
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals,key=lambda x: x.start)
        for i in range(0,len(intervals)):
            if len(result)==0:
                result.append(intervals[i])
                continue
            if intervals[i].start>result[-1].end:
                result.append(intervals[i])
                continue
            if intervals[i].end<=result[-1].end:
                continue
            result[-1].end = intervals[i].end
        return result
