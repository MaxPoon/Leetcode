class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		hold1 = hold2 = -99999
		release1 = release2 = 0
		for price in prices:
			release2 = max(release2, hold2+price)
			hold2 = max(hold2, release1-price)
			release1 = max(release1, hold1+price)
			hold1 = max(hold1, -price)
		return release2
