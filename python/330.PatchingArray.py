#With reference to the discussion: https://discuss.leetcode.com/topic/35494/solution-explanation/2
class Solution(object):
	def minPatches(self, nums, n):
		"""
		:type nums: List[int]
		:type n: int
		:rtype: int
		"""
		knownSum, i, patches = 0,0,0
		while knownSum<n:
			if i<len(nums) and nums[i]<=knownSum+1:
				knownSum += nums[i]
				i+=1
			else:
				knownSum = knownSum*2+1
				patches+=1
		return patches