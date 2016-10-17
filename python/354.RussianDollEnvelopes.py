class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n<2:
            return n
        envelopes = sorted(envelopes, lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        print(envelopes)
        dp =[1]*n
        g = [0x7fffffff] * (n + 1)
        for i in range(n):
            k = self.lower_bound(1,n+1, envelopes[i][1],g)
            dp[i]=k
            g[k]=envelopes[i][1]
        return max(dp)
        
    def lower_bound(self, L, R, x,arrays):
        while L < R:
            mid = (L + R) >> 1
            if x <= arrays[mid]:
                R = mid
            else:
                L = mid + 1
        return L
