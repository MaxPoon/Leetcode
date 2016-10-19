class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result=[]
        self.s = set([])
        def solve(prefix, suffix):
            if prefix == ():
                self.result.append(suffix)
            else:
                for i,n in enumerate(prefix):
                    if (suffix+tuple([n])) not in self.s:
                        self.s.add(suffix+tuple([n]))
                        solve(prefix[:i]+prefix[i+1:], suffix+tuple([n]))
        nums=tuple(nums)
        solve(nums,())
        return self.result
