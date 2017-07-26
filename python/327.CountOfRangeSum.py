class Solution(object):
	def countRangeSum(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: int
		"""
		first = [0]
		for num in nums:
			first.append(first[-1] + num)
		def sort(lo, hi):
			mid = (lo + hi) / 2
			if mid == lo:
				return 0
			count = sort(lo, mid) + sort(mid, hi)
			i = j = mid
			for left in first[lo:mid]:
				while i < hi and first[i] - left <  lower: i += 1
				while j < hi and first[j] - left <= upper: j += 1
				count += j - i
			first[lo:hi] = sorted(first[lo:hi])
			return count
		return sort(0, len(first))
