class Solution(object):
	def numWays(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: int
		"""
		if n==0: return 0
		if n==1: return k
		if n==2: return k*k
		e1, e2, e3, e4 = k-1, k-1, 1, 0
		x = n-2
		x = bin(x)[3:]
		for i in range(len(x)):
			e1, e2, e3, e4 = e1*e1 + e2*e3, e1*e2+e2*e4, e1*e3+e3*e4, e2*e3+e4*e4
			if x[i]=='1':
				e1, e2, e3, e4 = e1*(k-1)+e2, e1*(k-1), e3*(k-1)+e4, e3*(k-1)
		v1 = k*(k-1)
		v2 = k
		y1 = e1*v1+e2*v2
		y2 = e3*v1+e4*v2
		return y1+y2