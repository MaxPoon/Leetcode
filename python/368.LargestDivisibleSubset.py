class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        if len(nums) == 1: return [nums[0]]
        nums.sort()
        dp = [None] * len(nums)
        dp[0] = (1, None)
        for i in range(1, len(nums)):
            longest = (1, None)
            for j in range(0, i):
                if nums[i]%nums[j]!=0: continue
                if dp[j][0]+1 > longest[0]:
                    longest = (dp[j][0]+1, j)
            dp[i] = longest
        longestI, longest = 0, dp[0]
        for i, pair in enumerate(dp):
            if pair[0] > longest[0]:
                longest = pair
                longestI = i
        result = [nums[longestI]]
        i = longestI
        while dp[i][1] != None:
            i = dp[i][1]
            result.append(nums[i])
        return result
