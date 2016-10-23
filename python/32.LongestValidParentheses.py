class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 2:
            return 0
        stack, maxLen = 0,0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack += 1
            else:
                if stack > 0:
                    stack -= 1
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i] >= 0:
                        dp[i] += dp[i - dp[i]]
            
            maxLen = max(maxLen, dp[i])
        return maxLen
