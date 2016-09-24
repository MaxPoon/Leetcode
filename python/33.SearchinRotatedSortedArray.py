class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left =0
        right = len(nums)-1
        while(left<=right):
            if nums[left]==target:
                return left
            if nums[right] == target:
                return right
            mid = (left+right)/2
            if nums[mid]==target:
                return mid
            if((nums[mid]>target and target>nums[left] and nums[mid]>nums[left]) or (nums[mid]<nums[left] and (target<nums[mid] or target>nums[right]))):
                right = mid-1
            else:
                left = mid +1
        return -1
