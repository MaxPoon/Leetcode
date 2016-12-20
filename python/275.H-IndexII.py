class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		left, right = 0, len(citations)
		while left<right:
			mid = (left+right)//2
			if citations[mid]<len(citations)-mid:
				left = mid + 1
				
			elif citations[mid]==len(citations)-mid:
				return len(citations)- mid
			else:
				right = mid
		return len(citations)-left