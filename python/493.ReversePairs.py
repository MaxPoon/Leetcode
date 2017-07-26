class Solution(object):
	def reversePairs(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0
		def sort(start, end):
			if start == end:
				return 0
			if end - start == 1:
				count = 1 if nums[start] > 2*nums[end] else 0
				nums[start:end+1] = sorted(nums[start:end+1])
				return count
			mid = (start+end)//2
			count = sort(start, mid) + sort(mid+1, end)
			left = start
			right = mid
			while left <= mid:
				while right+1 <= end and nums[left]>2*nums[right+1]:
					right += 1
				count += right - mid
				left += 1
			nums[start:end+1] = sorted(nums[start:end+1])
			return count
		return sort(0, len(nums)-1)
