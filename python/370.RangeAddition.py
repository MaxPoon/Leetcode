class Solution(object):
	def getModifiedArray(self, length, updates):
		"""
		:type length: int
		:type updates: List[List[int]]
		:rtype: List[int]
		"""
		cache = [0] * length
		for update in updates:
			start, end, inc = tuple(update)
			cache[start] += inc
			if end+1 < length:
				cache[end+1] -= inc
		result = [0] * length
		result[0] = cache[0]
		for i in range(1, length):
			result[i] = result[i-1] + cache[i]
		return result
