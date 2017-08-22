class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort()
        left = points[-1][1] + 1
        count = 0
        for point in reversed(points):
            if point[1] < left:
                left = point[0]
                count += 1
        return count
