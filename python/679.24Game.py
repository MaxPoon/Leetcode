from operator import truediv, mul, add, sub
class Solution(object):
	def judgePoint24(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if not nums: return False
		if len(nums) == 1: return abs(nums[0] - 24) < 1e-6

		for i in xrange(len(nums)):
			for j in xrange(len(nums)):
				if i != j:
					B = [nums[k] for k in xrange(len(nums)) if i != k != j]
					for op in (truediv, mul, add, sub):
						if (op is add or op is mul) and j > i: continue
						if op is not truediv or nums[j]:
							B.append(op(nums[i], nums[j]))
							if self.judgePoint24(B): return True
							B.pop()
		return False
