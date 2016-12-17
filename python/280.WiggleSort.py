class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums.sort()
		mid = int((len(nums)+1)/2)
		small = nums[:mid]
		big = nums[mid:]
		p1, p2 =0, 0
		pushSmall = True
		newNums = []
		while p1<len(small) and p2 <len(big):
			if pushSmall:
				newNums.append(small[p1])
				p1+=1
			else: 
				newNums.append(big[p2])
				p2+=1
			pushSmall = not pushSmall
		if p1<len(small):newNums.append(small[p1])
		if p2<len(big):newNums.append(big[p2])
		for i in range(len(nums)):
			nums[i] = newNums[i]