class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left != right:
            mid = (left+right)//2
            if mid == 0 or mid == len(nums)-1:
                return nums[mid]
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
                return nums[mid]
            diff = 1
            if (mid-left)%2 == 0:
                diff = 2
            if (nums[mid] == nums[mid-1] and diff == 1) or (nums[mid] == nums[mid+1] and diff == 2):
                left = mid + diff
            else:
                right = mid - diff
        return nums[left]
