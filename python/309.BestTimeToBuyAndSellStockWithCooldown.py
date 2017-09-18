class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices: return 0
		coolDown = [0]*len(prices)
		hold = [-prices[0]]*len(prices)
		rest = [0]*len(prices)
		for i in range(1,len(prices)):
			coolDown[i] = max(hold[i-1]+prices[i], hold[i-1]+prices[i])
			hold[i] = max(hold[i-1], rest[i-1]-prices[i])
			rest[i] = max(rest[i-1], coolDown[i-1])
		return max(coolDown[-1], rest[-1])
