class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [h[target - nums[i]], i]
            h[nums[i]] = i
