from collections import deque

class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		q = deque()
		result = []
		for i, num in enumerate(nums):
			while len(q) and q[0][1] + k<=i:
				q.popleft()
			while len(q) and q[-1][0] <= num:
				q.pop()
			q.append((num,i))
			if i>=k-1:
				result.append(q[0][0])
		return result