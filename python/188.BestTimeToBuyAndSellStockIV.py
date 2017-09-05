class Solution(object):
	def maxProfit(self, k, prices):
		"""
		:type k: int
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) < 2 or k==0: return 0
		if k >= len(prices)//2:
			return self.maxProfitGreedy(prices)
		holds = [-9999]*k
		releases = [0]*k
		for j, price in enumerate(prices):
			for i in range(min((j+2)//2, k)-1, -1, -1):
				releases[i] = max(releases[i], holds[i]+price)
				if i != 0:
					holds[i] = max(holds[i], releases[i-1]-price)
				else:
					holds[i] = max(holds[i], -price)
		return max(releases)

	def maxProfitGreedy(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		total = 0
		for i in range(1, len(prices)):
			diff = prices[i] - prices[i-1]
			if diff > 0:
				total += diff
		return total
