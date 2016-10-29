class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		coins_set=set(coins)
		if amount == 0: return 0
		if min(coins_set)>amount: return -1
		dp = [-1]*min(coins_set) + [1]
		i = min(coins_set) + 1
		while i<=amount:
			if i in coins_set:
				dp.append(1)
				i+=1
				continue
			minimum = -1
			for coin in coins_set:
				if i-coin >0 and dp[i-coin]!=-1:
					temp = dp[i-coin]+1
					minimum = temp if minimum==-1 else min(temp,minimum)
			dp.append(minimum)
			i+=1
		return dp[amount]