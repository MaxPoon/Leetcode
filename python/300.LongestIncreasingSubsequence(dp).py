class Solution(object):

    def lengthOfLIS(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        if len(nums)==0:

            return 0

        f = [1]*len(nums)

        for i in range(len(nums)):

            if (i!=0):

                for j in range(i):

                    if(nums[i]>nums[j]):

                        f[i] = max(f[i], f[j]+1)

        return max(f)
