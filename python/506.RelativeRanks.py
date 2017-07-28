class Solution(object):
	def findRelativeRanks(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		numsWithIndex = [(num, i)for i, num in enumerate(nums)]
		numsWithIndex.sort(reverse=True)
		result = [0]*len(nums)
		medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		for j, (num, i) in enumerate(numsWithIndex):
			result[i] = medals[j] if j < 3 else str(j+1)
		return result
