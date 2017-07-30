class NumArray(object):
	def __init__(self, nums):
		self.n = len(nums)
		self.a, self.c = [0]*self.n, [0] * (self.n + 1)
		for i, num in enumerate(nums):
			self.update(i, num)

	def update(self, i, val):
		diff, self.a[i] = val - self.a[i], val
		i += 1
		while i <= self.n:
			self.c[i] += diff
			i += (i & -i)

	def sumRange(self, i, j):
		res, j = 0, j + 1
		while j:
			res += self.c[j]
			j -= (j & -j)
		while i:
			res -= self.c[i]
			i -= (i & -i)
		return res
		


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)