def search(positive, negative, current):
	if len(positive)==1:
		return len(negative)+current
	if len(negative)==1:
		return len(positive)+current
	minimum = current + len(negative)* len(positive)
	p = positive[-1]
	
	for i, n in enumerate(negative):
		if p+n==0:
			newPositive = positive[:-1]
			newNegative = negative[:i] + negative[i+1:]
			minimum = search(newPositive, newNegative, current+1)
			return minimum
			
	for i in range(len(negative)):
		n = negative[i]
		if -n<p:
			newPositive = positive[:]
			newPositive[-1] += n
			newNegative = negative[:i] + negative[i+1:]
		else:
			newPositive = positive[:-1]
			newNegative = negative[:]
			newNegative[i] += p
			
		minimum = min(minimum, search(newPositive, newNegative, current+1))
	return minimum
			

class Solution(object):
	def minTransfers(self, transactions):
		"""
		:type transactions: List[List[int]]
		:rtype: int
		"""
		balance = {}
		for x,y,z in transactions:
			if x in balance:
				balance[x] += z
			else: balance[x] = z
			if y in balance:
				balance[y]-=z
			else: balance[y] = -z
		positive, negative = [], []
		for n in balance.values():
			if n>0: positive.append(n)
			if n<0: negative.append(n)
		if len(positive)==0: return 0
		if len(positive)==1:
			return len(negative)
		if len(negative)==1:
			return len(positive)
		return search(positive, negative, 0)