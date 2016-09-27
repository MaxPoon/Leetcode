class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l<3:
            return 0
        highest = max(height)
        highestIndex = height.index(highest)
        leftHighest = 0
        rightHighest = 0
        result = 0
        for i in range(highestIndex):
            if(leftHighest-height[i])>0:
                result+=leftHighest-height[i]
            else:
                leftHighest = height[i]
        for i in range(l-1,highestIndex,-1):
            if(rightHighest-height[i])>0:
                result+=rightHighest-height[i]
            else:
                rightHighest = height[i]
        return result
