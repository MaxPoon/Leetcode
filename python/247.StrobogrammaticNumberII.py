def formPrefix(prefix, length, prefixes, isOdd):
	if len(prefix) == length: 
		prefixes.append(prefix)
		return
	if len(prefix)!=0:
		formPrefix(prefix+"0", length, prefixes, isOdd)
	formPrefix(prefix+"1", length, prefixes, isOdd)
	if not isOdd or len(prefix)+1<length:
		formPrefix(prefix+"6", length, prefixes, isOdd)
	formPrefix(prefix+"8", length, prefixes, isOdd)
	if not isOdd or len(prefix)+1<length:
		formPrefix(prefix+"9", length, prefixes, isOdd)
	

class Solution(object):
	def findStrobogrammatic(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		if n==1: return ["0","1","8"]
		rotate ={"0":"0", "1":"1", "6":"9", "8":"8", "9": "6"}
		results = [] 
		mid = (n+1)//2
		formPrefix("", mid, results, n&1==1)
		if n&1==1:
			mid -= 2
		else: mid-=1
		for i in range(len(results)):
			for j in range(mid, -1, -1):
				results[i] += rotate[results[i][j]]
		return results
			