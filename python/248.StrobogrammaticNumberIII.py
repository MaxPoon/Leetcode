def formPrefixLowHigh(prefix, length, isOdd, low, high, rotate):
	if length==1 and isOdd:
		return len([1 for n in ("0", "1", "8") if n>=low and n<=high])
	if prefix < low[:len(prefix)] or prefix>high[:len(prefix)]: return 0
	if len(prefix) == length: 
		if prefix < low[:len(prefix)] or prefix>high[:len(prefix)]: return 0
		l = length-2 if isOdd else length-1
		for i in range(l, -1, -1):
			prefix += rotate[prefix[i]]
		if prefix>=low and prefix <= high: return 1
		else: return 0
	total = 0
	if len(prefix)!=0:
		total += formPrefixLowHigh(prefix+"0", length, isOdd, low, high, rotate)
	total += formPrefixLowHigh(prefix+"1", length, isOdd, low, high, rotate)
	if not isOdd or len(prefix)+1<length:
		total += formPrefixLowHigh(prefix+"6", length, isOdd, low, high, rotate)
		total += formPrefixLowHigh(prefix+"9", length, isOdd, low, high, rotate)
	total += formPrefixLowHigh(prefix+"8", length, isOdd, low, high, rotate)
	return total
		

class Solution(object):
	def strobogrammaticInRange(self, low, high):
		"""
		:type low: str
		:type high: str
		:rtype: int
		"""
		l1 = len(low)
		l2 = len(high)
		rotate ={"0":"0", "1":"1", "6":"9", "8":"8", "9": "6"}
		if l1>l2 or (l1==l2 and low>high): return 0
		if l1==l2:
			mid = (l1+1)//2
			result = formPrefixLowHigh("", mid, l1&1==1, low, high,rotate)
			return result
		mid = (l1+1)//2
		result = formPrefixLowHigh("", mid, l1&1==1, low, "9"*l1, rotate)
		mid = (l2+1)//2
		result += formPrefixLowHigh("", mid, l2&1==1, "0"*l2, high, rotate)
		for l in range(l1+1,l2):
			mid = (l+1)//2
			result += formPrefixLowHigh("", mid, l&1==1, "0", "9"*l, rotate)
		return result