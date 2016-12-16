def generateString(lower, upper):
	if lower +2 >upper: return None
	if lower +2 ==upper:
		return str(lower+1)
	else: return str(lower+1)+"->"+str(upper-1)
	
class Solution(object):
	def findMissingRanges(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: List[str]
		"""
		result = []
		if len(nums)==0:
			newString = generateString(lower-1,upper+1)
			if newString:
				result.append(newString)
			return result
		if len(nums)==1:
			newString = generateString(lower-1,nums[0])
			if newString:
				result.append(newString)
			newString = generateString(nums[0],upper+1)
			if newString:
				result.append(newString)
			return result
		newString = generateString(lower-1,nums[0])
		if newString:
			result.append(newString)
		for i in range(1,len(nums)):
			newString = generateString(nums[i-1],nums[i])
			if newString:
				result.append(newString)
		newString = generateString(nums[-1], upper+1)
		if newString:
			result.append(newString)
		return result