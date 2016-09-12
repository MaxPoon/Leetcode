class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        else:
            dp[0]=nums[0]
            dp[1]=nums[1]
            for i in range(2,n):
                dp[i]=max(dp[:i-1])+nums[i]
            return max(dp)
