class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		if len(citations)==0: return 0
		citations.sort(reverse=True)
		for i, citation in enumerate(citations, start=1):
			if citation<i:break
		if citations[i-1] < i: i-=1
		return i