class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums=nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        n=0
        for i in range(len(self.nums)):
            if (self.nums[i]==target):
                n=n+1
        m=1
        r=random.randrange(1,n+1)
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                if m==r:
                    return i 
                m=m+1

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
