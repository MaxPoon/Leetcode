class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        for x in nums1:
            if x not in map:
                map[x] = 1
            else:
                map[x] += 1

        res = []
        for y in nums2:
            if y in map and map[y] > 0:
                res.append(y)
                map[y] -= 1

        return res
