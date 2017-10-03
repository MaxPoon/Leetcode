class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A,E)
        right = max(min(C,G), left)
        bottom = max(B,F)
        top = max(min(D,H), bottom)
        return (C-A)*(D-B) - (right-left)*(top-bottom) + (G-E)*(H-F)
