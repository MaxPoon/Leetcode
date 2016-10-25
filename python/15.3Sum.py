class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3: return []
        h={}
        result=[]
        for i,n in enumerate(nums):
            if n in h:
                h[n]+=1
            else:
                h[n]=1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                s=nums[i]+nums[j]
                if -s in h:
                    temp = [nums[i],nums[j],-s]
                    if temp.count(-s)<=h[-s]:result.append(tuple(sorted(temp)))
        return list(set(result))