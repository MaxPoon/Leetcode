class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        numbers = set()
        for index in (0,1,3,4):
            numbers.add(int(time[index]))
        timeInMin = int(time[:2])*60 + int(time[3:])
        oneDayInMin = 24*60
        minGap = oneDayInMin
        nextClosest = time
        for h1 in numbers:
            if h1 > 2: continue
            for h2 in numbers:
                if h1 == 2 and h2 > 4: continue
                for m1 in numbers:
                    if m1 > 5: continue
                    for m2 in numbers:
                        gap = (h1*10+h2)*60+m1*10+m2 - timeInMin
                        if gap <= 0:
                            gap += oneDayInMin
                        if gap < minGap:
                            minGap = gap
                            nextClosest = str(h1)+str(h2)+':'+str(m1)+str(m2)
        return nextClosest
