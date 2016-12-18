class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		intervals = []
		for num in nums:
			if not intervals or num-intervals[-1][1]>1:
				intervals.append([num,num])
			else:
				intervals[-1][1] = num
		for i in range(len(intervals)):
			if intervals[i][0] == intervals[i][1]:
				intervals[i] = str(intervals[i][0])
			else:
				intervals[i] = str(intervals[i][0]) + "->" + str(intervals[i][1])
		return intervals