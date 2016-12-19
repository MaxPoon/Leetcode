class Solution(object):
	def sortTransformedArray(self, nums, a, b, c):
		"""
		:type nums: List[int]
		:type a: int
		:type b: int
		:type c: int
		:rtype: List[int]
		"""
		if a==0:
			if b==0: return [c]*len(nums)
			result = map(lambda x:b*x+c, nums)
			if b>0:
				return result
			else:
				return result[::-1]
		k = -b/a/2.0
		result = [0] * len(nums)
		p1 = 0 
		p2 = len(nums)-1
		i = 0
		while p1<=p2:
			n1 = nums[p1]
			n2 = nums[p2]
			if abs(n1-k)<abs(n2-k):
				result[i] = a*n2**2 + b*n2 + c
				p2 -= 1
			else:
				result[i] = a*n1**2 + b*n1 + c
				p1 += 1
			i += 1
		if a>0:
			result.reverse()
		return result