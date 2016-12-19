class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.smallAmount = 0
		


class Solution(object):
	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if len(nums)==0: return []
		result = [0]
		self.root = Node(nums[-1])
		for i in range(len(nums)-2, -1, -1):
			self.addNum(nums[i], result)
		result.reverse()
		return result
		
	def addNum(self, num, result):
		"""
		Adds a num into the data structure.
		:type num: int
		:rtype: void
		"""
		smaller = 0
		node = self.root
		while True:
			if num < node.val: 
				node.smallAmount += 1
				if node.left:
					node = node.left
				else:
					node.left = Node(num)
					result.append(smaller)
					return
			else:
				smaller += node.smallAmount + (1 if num > node.val else 0 )
				if node.right:
					node = node.right
				else:
					node.right = Node(num)
					result.append(smaller)
					return