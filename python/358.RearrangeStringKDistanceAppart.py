from heapq import heappush, heappop
class Solution(object):
	def rearrangeString(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: str
		"""
		if k==0:
			return s
		newOrder = [None]*len(s)
		letterCount = {}
		heap = []
		toBePushed = {}
		for c in s:
			letterCount[c] = letterCount.get(c, 0) + 1
		for c, count in letterCount.items():
			heappush(heap, (-count, c))
		for i in range(len(s)):
			if i >= k:
				c = newOrder[i-k]
				if (toBePushed[c]<0):
					heappush(heap, (toBePushed[c], c))
			if not heap:
				return ""
			count, c = heappop(heap)
			toBePushed[c] = count+1
			newOrder[i] = c
		return "".join(newOrder)
