class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		index = {}
		for i, num in enumerate(nums):
			if num not in index:
				index[num] = [i]
			else:
				for j in index[num]:
					if abs(j-i)<=k: return True
				index[num].append(i)
		return False