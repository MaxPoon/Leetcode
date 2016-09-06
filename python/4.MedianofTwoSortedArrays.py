class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n%2 == 0:
            return (self.findKth(n/2,nums1,nums2)+self.findKth(n/2+1,nums1,nums2))/2.0
        else:
            return self.findKth(n//2+1, nums1,nums2)
            
    def findKth(self,k,A,B):
        if len(A) == 0:
            return B[k-1]
        elif len(B) == 0:
            return A[k-1]
        elif k == 1:
            return min(A[0], B[0])
        if len(A)<k/2:
            return self.findKth(k-k/2,A,B[k/2:])
        if len(B)<k/2:
            return self.findKth(k-k/2,A[k/2:],B)
        a = A[k/2-1]
        b = B[k/2-1]
        if a>=b:
            return self.findKth(k-k/2,A,B[k/2:])
        if a<b:
            return self.findKth(k-k/2,A[k/2:],B)
