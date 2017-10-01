class Solution(object):
	def nextGreaterElements(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums: return []
		maxNum = max(nums)
		i = nums.index(maxNum)
		result = [-1]*len(nums)
		result[i] = -1
		stack = [maxNum]
		for j in range(i-1, i-len(nums), -1):
			num = nums[j]
			while stack and stack[-1] <= num:
				stack.pop()
			if stack:
				result[j] = stack[-1]
			stack.append(num)
		return result
