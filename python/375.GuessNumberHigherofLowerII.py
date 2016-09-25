class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0 or n==1):
            return 0
        dp=[] #dp[i][j]: how much money you need to have to guarantee a win if the number is in [i,j]
        for i in range(n+1):
            dp.append([])
            for j in range(n+1):
                if (i==j):
                    dp[i].append(0)
                else:
                    dp[i].append(None)
        for i in range(n-1,0,-1):
            for j in range(i+1,n+1):
                minimum = min(dp[i+1][j]+i,dp[i][j-1]+j)
                for k in range(i+1,j):
                    temp = max(k+dp[i][k-1],k+dp[k+1][j])
                    if temp<minimum:
                        minimum = temp
                dp[i][j]=minimum
        return dp[1][n]
