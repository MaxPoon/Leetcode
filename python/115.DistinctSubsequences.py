class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        dp=[] #dp[i][j]: distinct subsequences of t[:i+1] in s[:j+1]
        for i in range(0,len(t)):
            dp.append([])
            for j in range(len(s)):
                if j==0 and i==0:
                    if s[0]==t[0]:
                        dp[0].append(1)
                    else:
                        dp[0].append(0)
                    continue
                if j<i or j==0:
                    dp[i].append(0)
                    continue
                if(s[j]!=t[i]):
                    dp[i].append(dp[i][j-1])
                else:
                    if(i==0):
                        dp[i].append(dp[i][j-1]+1)
                    else:
                        dp[i].append(dp[i][j-1]+dp[i-1][j-1])
        return dp[len(t)-1][len(s)-1]
