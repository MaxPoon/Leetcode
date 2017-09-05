class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices: return 0
		dp1 = [0]*len(prices)
		dp2 = [0]*len(prices)
		currentMin = prices[0]
		for i in range(1, len(prices)):
			dp1[i] = prices[i] - currentMin
			dp1[i] = max(dp1[i-1], dp1[i])
			currentMin = min(currentMin, prices[i])
		currentMax = prices[-1]
		for i in range(len(prices)-2, -1, -1):
			dp2[i] = currentMax - prices[i]
			dp2[i] = max(dp2[i], dp2[i+1])
			currentMax = max(currentMax, prices[i])
		result = 0
		for i in range(len(prices)):
			result = max(result, dp1[i]+dp2[i])
		return result
