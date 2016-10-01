# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.summary = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if len(self.summary)==0:
            self.summary = [Interval(val,val)]
            return
        if val<self.summary[0].start:
            if val == self.summary[0].start-1:
                self.summary[0].start=self.summary[0].start-1
            else:
                self.summary = [Interval(val,val)]+self.summary
        elif val>self.summary[len(self.summary)-1].end:
            if val == self.summary[len(self.summary)-1].end+1:
                self.summary[len(self.summary)-1].end=self.summary[len(self.summary)-1].end+1
            else:
                self.summary = self.summary+[Interval(val,val)]
        left = 0
        right = len(self.summary)-1
        while left!=right:
            if (right-left==1):
                if val<self.summary[left].end or val>self.summary[right].start:
                    return
                elif val==self.summary[left].end+1 and val==self.summary[right].start-1:
                    self.summary = self.summary[:left]+[Interval(self.summary[left].start,self.summary[right].end)]+self.summary[right+1:]
                elif val==self.summary[left].end+1:
                    self.summary = self.summary[:left]+[Interval(self.summary[left].start,val)]+self.summary[right:]
                elif val==self.summary[right].start-1:
                    self.summary = self.summary[:left+1]+[Interval(val,self.summary[right].end)]+self.summary[right+1:]
                elif val>self.summary[left].end+1 and val<self.summary[right].start-1:
                    self.summary = self.summary[:left+1]+[Interval(val,val)]+self.summary[right:]
                break
            mid = (left+right)/2
            if val<self.summary[mid].start:
                right = mid
            elif val>self.summary[mid].end:
                left = mid
            else:
                break
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.summary


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
