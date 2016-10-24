class Solution(object):
	def candy(self, ratings):
		"""
		:type ratings: List[int]
		:rtype: int
		"""
		l=len(ratings)
		if l==1 or l==0:
			return l
		candies = [1]*l
		for i in range(1,l):
			if ratings[i]>ratings[i-1]:
				candies[i]=candies[i-1]+1
		for i in range(l-2,-1,-1):
			if ratings[i]>ratings[i+1] and candies[i]<=candies[i+1]:
				candies[i]=candies[i+1]+1
		return sum(candies)