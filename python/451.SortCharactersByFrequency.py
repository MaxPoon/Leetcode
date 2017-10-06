from collections import Counter
class Solution(object):
	def frequencySort(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		counter = Counter(s)
		characterSet = []
		for k,v in counter.items():
			characterSet.append(k*v)
		characterSet.sort(key=lambda x:len(x), reverse=True)
		return ''.join(characterSet)
