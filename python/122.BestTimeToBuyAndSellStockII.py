class Solution(object):
	def maxProfit(self, prices):
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
