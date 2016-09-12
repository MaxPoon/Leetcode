class Solution(object):
    def integerBreak(self, n):
        if n <= 3 :return n-1
        mod = n % 3
        if mod == 0: return pow(3, n / 3)
        if mod == 1: return 4 * pow(3, (n - 4) / 3)
        return 2 * pow(3, n / 3)
