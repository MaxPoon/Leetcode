class Solution(object):
	def maxVacationDays(self, flights, days):
		"""
		:type flights: List[List[int]]
		:type days: List[List[int]]
		:rtype: int
		"""
		numOfCities = len(flights)
		numOfWeeks = len(days[0])
		dp = [[-1]*numOfCities for _ in range(numOfWeeks)]
		dp[0][0] = days[0][0]
		for nextCity in range(numOfCities):
			if flights[0][nextCity]:
				dp[0][nextCity] = days[nextCity][0]
		for week in range(0, numOfWeeks-1):
			for city in range(numOfCities):
				if dp[week][city] == -1: continue
				for nextCity in range(numOfCities):
					if nextCity == city or flights[city][nextCity]:
						dp[week+1][nextCity] = max(dp[week+1][nextCity], dp[week][city]+days[nextCity][week+1])
		return max(dp[-1])
