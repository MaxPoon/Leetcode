class Solution(object):
	def findPermutation(self, s):
		"""
		:type s: str
		:rtype: List[int]
		"""           
		i = -1
		pointer = 0
		lastNum = 0
		result = [0]*(len(s)+1)
		while i < len(s):
			j = i + 1
			while j < len(s):
				if s[j] == 'I':
					break
				j += 1
			for num in range(lastNum + j-i, lastNum, -1):
				result[pointer] = num
				pointer += 1
			lastNum = lastNum + j - i
			i = j
		return result
