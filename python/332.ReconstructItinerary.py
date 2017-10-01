from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		fromTo = defaultdict(list)
		for ticket in tickets:
			heappush(fromTo[ticket[0]], ticket[1])
		self.fromTo = fromTo
		self.itinerary = []
		self.dfs('JFK')
		return list(reversed(self.itinerary))

	def dfs(self, currentCity):
		while self.fromTo[currentCity]:
			nextCity = heappop(self.fromTo[currentCity])
			self.dfs(nextCity)
		self.itinerary.append(currentCity)
