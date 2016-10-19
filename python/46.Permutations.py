class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        def solve(prefix, suffix):
            if prefix == []:
                self.result.append(suffix)
            else:
                for i,n in enumerate(prefix):
                    solve(prefix[:i]+prefix[i+1:], suffix+[n])
        
        solve(nums, [])
        return self.result
