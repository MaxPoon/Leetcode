class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2 or n==3:
            return max(nums)
        dp1=[0]*(n-1)
        dp2=[0]*(n-1)
        nums1=nums[:n-1]
        nums2=nums[1:]
        dp1[0]=nums1[0]
        dp1[1]=nums1[1]
        dp2[0]=nums2[0]
        dp2[1]=nums2[1]
        for i in range(2,n-1):
            dp1[i]=max(dp1[:i-1])+nums1[i]
            print(dp1)
            dp2[i]=max(dp2[:i-1])+nums2[i]
        return max(max(dp1),max(dp2))
