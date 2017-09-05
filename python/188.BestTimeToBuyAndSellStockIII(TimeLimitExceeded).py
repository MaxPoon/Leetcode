class Solution(object):
	def maxProfit(self, k, prices):
		"""
		:type k: int
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) < 2 or k==0: return 0
		maxTransactionTimes = min(k, len(prices)//2)
		holds = [-9999]*maxTransactionTimes
		releases = [0]*maxTransactionTimes
		for j, price in enumerate(prices):
			for i in range(min((j+2)//2, maxTransactionTimes)-1, -1, -1):
				releases[i] = max(releases[i], holds[i]+price)
				if i != 0:
					holds[i] = max(holds[i], releases[i-1]-price)
				else:
					holds[i] = max(holds[i], -price)
		return max(releases)
