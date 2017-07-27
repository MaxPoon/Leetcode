def isSubsequence(string1, string2, m, n):
	# Base Cases
	if m == 0:    return True
	if n == 0:    return False
 
	# If last characters of two strings are matching
	if string1[m-1] == string2[n-1]:
		return isSubsequence(string1, string2, m-1, n-1)
 
	# If last characters are not matching
	return isSubsequence(string1, string2, m, n-1)

class Solution(object):
	def findLUSlength(self, strs):
		"""
		:type strs: List[str]
		:rtype: int
		"""
		strs.sort(key=lambda s: (len(s), s), reverse=True)
		counts = {}
		for string in strs:
			counts[string] = counts.get(string, 0) + 1
		for i, string in enumerate(strs):
			if counts[string] != 1: continue
			if not any([len(string) < str(strs[j]) and isSubsequence(string, strs[j], len(string), len(strs[j])) for j in range(i)]):
				return len(string)
		return -1
