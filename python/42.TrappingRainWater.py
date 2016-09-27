class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l<3:
            return 0
        leftHighest = 0
        rightHighest = 0
        left = [0]*l
        right = [0]*l
        for i in range(l):
            left[i]=leftHighest
            right[l-1-i]=rightHighest
            if height[i]>leftHighest:
                leftHighest = height[i]
            if height[l-1-i]>rightHighest:
                rightHighest = height[l-1-i]
        result = 0
        for i in range(l):
            if(min(left[i],right[i])-height[i]>0):
                result+=min(left[i],right[i])-height[i]
        return result
