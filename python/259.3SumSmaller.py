class Solution(object):
	def threeSumSmaller(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if len(nums)<3: return 0
		nums.sort()
		i = 0
		ans = 0
		while i<len(nums)-2:
			k = len(nums)-1
			j = i + 1
			while k>j:
				ans += j-i-1
				while nums[i]+nums[j]+nums[k] < target:
					ans += 1
					if j<k-1:
						j+=1
					else: break
				k-=1
			ans += (j-i-1)*(j-i)/2
			i+=1
		return ans