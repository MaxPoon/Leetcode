class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        pop = 0
        for c in num:
            while stack and pop < k and c < stack[-1]:
                stack.pop()
                pop += 1
            stack.append(c)
        leadingZeroIndex = -1
        for i, c in enumerate(stack):
            if c == '0':
                leadingZeroIndex = i
            else:
                break
        result = ''.join(stack[leadingZeroIndex+1:len(num)-k])
        if not result: return '0'
        return result402. Remove K Digits
