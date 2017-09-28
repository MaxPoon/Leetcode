cache = {}
class Solution(object):
	def countArrangement(self, N):
		def helper(i, X):
			if i == 1:
				return 1
			key = (i, X)
			if key in cache:
				return cache[key]
			total = 0
			for j in xrange(len(X)):
				if X[j] % i == 0 or i % X[j] == 0:
					total += helper(i - 1, X[:j] + X[j + 1:])
			cache[key] = total
			return total
		return helper(N, tuple(range(1, N + 1)))
