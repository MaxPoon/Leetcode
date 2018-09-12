class MyCalendarThree:

    def __init__(self):
        self.delta = {}
        self.sortedTime = []
    
    def addTime(self, time):
        index = len(self.sortedTime)
        for i, value in enumerate(self.sortedTime):
            if value == time:
                return
            if value > time:
                index = i
                break
        self.sortedTime = self.sortedTime[:index] + [time] + self.sortedTime[index:]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1
        self.addTime(start)
        self.addTime(end)
        active = ans = 0
        for x in self.sortedTime:
            active += self.delta[x]
            if active > ans: ans = active
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)