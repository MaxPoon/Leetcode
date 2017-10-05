class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n >>= 1
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn
