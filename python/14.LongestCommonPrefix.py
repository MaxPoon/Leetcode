class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		from itertools import takewhile,izip

		def allsame(x):
			return len(set(x)) == 1
		
		r = "".join([i[0] for i in takewhile(allsame ,izip(*strs))])
		return r