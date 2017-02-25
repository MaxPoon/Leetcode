class Solution(object):
	def licenseKeyFormatting(self, S, K):
		"""
		:type S: str
		:type K: int
		:rtype: str
		"""
		key = "".join(S.split('-')).upper()
		result = ""
		for i in range(len(key), 0, -K):
			result = key[i-K if i-K > 0 else 0: i] + "-" + result
		return result.strip('-')