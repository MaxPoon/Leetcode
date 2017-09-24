class NumArray(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		if not nums:
			self.prefixSum = []
			return
		self.prefixSum = [0]*len(nums)
		self.prefixSum[0] = nums[0]
		for i in range(1, len(nums)):
			self.prefixSum[i] = self.prefixSum[i-1]+nums[i]

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		
		result = self.prefixSum[j]
		if i != 0:
			result -= self.prefixSum[i-1]
		return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)