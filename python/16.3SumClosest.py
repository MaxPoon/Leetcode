class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result=nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            temp_target = target-nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                temp = nums[j]+nums[k]-temp_target
                if temp==0:
                    return target
                if abs(temp) < abs(result-target):
                    result = nums[i]+nums[j]+nums[k]
                if temp<0: j+=1
                else: k-=1
        return result