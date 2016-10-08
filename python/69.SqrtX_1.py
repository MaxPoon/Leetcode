class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def mySqrt(self, x):
        start, end = 1, x
        while start + 1 < end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start
