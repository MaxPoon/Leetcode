class Solution(object):
	def numberOfArithmeticSlices(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		if len(A) < 3: return 0
		total = 0
		count = 0    
		diff = A[1] - A[0]
		for i in range(2, len(A)):
			newDiff = A[i] - A[i-1]
			if diff == newDiff:
				count += 1
				total += count
			else:
				count = 0
				diff = newDiff
		return total
