class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
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
        
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
        maxArea = 0
        if len(matrix)==1:
            temp = 0
            for i in range(len(matrix[0])):
                if matrix[0][i]:
                    if temp:
                        temp+=1
                    else:
                        temp=1
                else:
                    maxArea = max(temp, maxArea)
                    temp = 0
            if temp:
                maxArea = max(maxArea,temp)
            return maxArea
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[i])):
                if matrix[i][j]: matrix[i][j]+=matrix[i+1][j]
        i=0
        while maxArea<(len(matrix)-i)*len(matrix[0]) and i <len(matrix):
            maxArea = max(maxArea, largestRectangleArea(matrix[i]))
            i+=1
        return maxArea
