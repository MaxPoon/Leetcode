class NumArray(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		self.sums = {}
		if self.nums:
			self.initRecursion(0, len(nums)-1)
		
	def initRecursion(self, start, end):
		if start == end:
			return self.nums[start]
		if start + 1 == end:
			s = self.nums[start] + self.nums[end]
		else:
			mid = (start+end)//2
			s = self.initRecursion(start, mid) + self.initRecursion(mid + 1, end)
		self.sums[(start, end)] = s
		return s

	def update(self, i, val):
		"""
		:type i: int
		:type val: int
		:rtype: void
		"""
		diff = val - self.nums[i]
		self.nums[i] = val
		self.updateRecursion(i, diff, 0, len(self.nums)-1)
		
	def updateRecursion(self, i, diff, start, end):
		if start == end: return
		self.sums[(start, end)] += diff
		mid = (start+end)//2
		nextStart, nextEnd = (start, mid) if i <= mid else (mid+1, end)
		if nextStart != nextEnd:
			self.updateRecursion(i, diff, nextStart, nextEnd)

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		return self.sumRangeRecursion(i, j, 0, len(self.nums)-1)
	
	def sumRangeRecursion(self, i, j, start, end):
		if i > end or j < start: return 0
		if i < start: return self.sumRangeRecursion(start, j, start, end)
		if j > end: return self.sumRangeRecursion(i, end, start, end)
		if i == j: return self.nums[i]
		if i == start and j == end: return self.sums[(start, end)]
		mid = (start+end)//2
		return self.sumRangeRecursion(i, j, start, mid) + self.sumRangeRecursion(i, j, mid+1, end)
		


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)