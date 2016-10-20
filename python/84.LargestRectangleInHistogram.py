class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = len(heights)
        if l==0:
            return 0
        stack = [0]
        maxArea = 0
        for i in range(1,l):
            if len(stack)==0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
            # elif len(stack)>0 and heights[i]==heights[stack[-1]]:
            #     stack[-1] = i
            else:
                while( len(stack) and heights[i]<heights[stack[-1]]):
                    top = stack.pop()
                    area = heights[top]*(i-stack[-1]-1) if len(stack) else heights[top]*i
                    maxArea = max(maxArea, area)
                stack.append(i)
        for i,p in enumerate(stack):
            h = heights[p]
            if i==0:
                w = l
            else:
                w = l - stack[i-1]-1
            area = h*w
            maxArea=max(area,maxArea)
        return maxArea
