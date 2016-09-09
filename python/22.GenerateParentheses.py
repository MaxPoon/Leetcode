class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def backtracking(s, left, right):
            if len(s) == length:
                result.append(s)
            else:
                if left<n:
                    backtracking(s+"(",left+1, right)
                if right<left:
                    backtracking(s+")", left, right+1)
        
        if n==0:
            return []
        result = []
        length = 2*n
        backtracking("(",1,0)
        return result
