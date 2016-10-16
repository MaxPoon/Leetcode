class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solve(nums0, nums1, mask):
            if mask <= 1: return mask

            mask /= 2
            nums01 = [n for n in nums0 if n & mask]
            nums00 = [n for n in nums0 if not n & mask]
            nums11 = [n for n in nums1 if n & mask]
            nums10 = [n for n in nums1 if not n & mask]

            ans = 0
            if nums10 and nums01:
                ans = max(ans, solve(nums10, nums01, mask))
            if nums00 and nums11:
                ans = max(ans, solve(nums00, nums11, mask))
            if not ans:
                ans = solve(nums0, nums1, mask) - mask
            return ans + mask * 2
        mask = 1 << 31
        while mask:
            nums0 = [n for n in nums if not n & mask]
            nums1 = [n for n in nums if n & mask]
            if nums0 and nums1: break
            mask >>= 1
        return solve(nums0, nums1, mask)
