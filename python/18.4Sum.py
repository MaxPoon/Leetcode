class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        sums={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = nums[i]+nums[j]
                if s not in sums:
                    sums[s] = [[i,j]]
                else:
                    sums[s]+=[[i,j]]
        L = list(sums.keys())
        for k in L:
            if k in sums:
                v = sums[k]
                k2 = target -k
                if k==k2:
                    for i in range(len(v)):
                        for j in range(i+1,len(v)):
                            p1 = v[i]
                            p2 = v[j]
                            if len(set(p1+p2))==4:
                                l = sorted([nums[p1[0]],nums[p1[1]],nums[p2[0]],nums[p2[1]]])
                                if l not in result:
                                    result.append(l)
                    del sums[k]
                            
                if k2 not in sums:
                    continue
                if k != k2:
                    v2 = sums[k2]
                    for i in v:
                        for j in v2:
                            if len(set(i+j))==4:
                                l = sorted([nums[i[0]],nums[i[1]],nums[j[0]],nums[j[1]]])
                                if l not in result:
                                    result.append(l)
                    del sums[k]
                    del sums[k2]
        return result
