class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
 
        n = len(nums)
        dp, g = [1] * n, [sys.maxint] * (n + 2)
        for i in xrange(n):
            k = self.lower_bound(1,n+1,nums[i],g)
            dp[i] = k
            g[k] = nums[i]
        return max(dp)
 
    def lower_bound(self,L, R, x,g):
        while L < R:
            mid = (L + R) >> 1
            if g[mid] < x:
                L = mid + 1
            else:
                R = mid
        return L
