class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        size = len(nums)
        high = sum(nums)
        low = max(max(nums), high/m)
        while low <= high:
            mid = (low + high) / 2
            n = m
            cnt = 0
            valid = True
            for x in range(size):
                if cnt + nums[x] > mid:
                    n -= 1
                    cnt = 0
                cnt += nums[x]
                if n == 0:
                    valid = False
                    break
            if valid:
                high = mid - 1
            else:
                low = mid + 1
        return low
