class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = mask = 0
        for x in range(31, -1, -1):
            mask += 1 << x
            prefixSet = set([n & mask for n in nums])
            print(prefixSet)
            tmp = ans | 1 << x
            for prefix in prefixSet:
                if tmp ^ prefix in prefixSet:
                    ans = tmp
                    break
        return ans
