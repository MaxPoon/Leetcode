class Solution(object):
	def shoppingOffers(self, price, special, needs):
		"""
		:type price: List[int]
		:type special: List[List[int]]
		:type needs: List[int]
		:rtype: int
		"""
		d = {}
		def dfs(cur):
			val = sum(cur[i]*price[i] for i in range(len(needs)))
			for spec in special:
				tmp = [cur[j] - spec[j] for j in range(len(needs))]
				if min(tmp) >= 0:
					val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1])
			d[tuple(cur)] = val
			return val
		return dfs(needs)
