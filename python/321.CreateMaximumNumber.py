class Solution(object):
	def maxNumber(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[int]
		"""
		def selectKfromOne(nums, k):
			if k==0: return []
			stack = []
			for i in range(len(nums)):
				if len(stack)+len(nums)-i==k: 
					stack = stack+nums[i:]
					break
				if not len(stack): stack.append(nums[i])
				elif stack[-1]>=nums[i]: 
					if len(stack)<k:stack.append(nums[i])
					else: continue
				else:
					while len(stack) and stack[-1]<nums[i] and len(stack)+len(nums)-i>k:
						stack.pop()
					stack.append(nums[i])
			return stack
			
		result = []
		for i in range(len(nums1)+1):
			if k-i>len(nums2): continue
			n1 = selectKfromOne(nums1,i)
			n2 = selectKfromOne(nums2, k-i)
			temp = [max(n1, n2).pop(0) for i in range(k)]
			result = max(result, temp)
		return result