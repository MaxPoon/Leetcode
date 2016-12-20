# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def closestValue(self, root, target):
		"""
		:type root: TreeNode
		:type target: float
		:rtype: int
		"""
		node = root
		result = root.val
		while True:
			if target==node.val: return node.val
			elif target > node.val:
				if target-node.val < abs(result - target):
					result = node.val
				if node.right:
					node = node.right
				else:
					return result
			else:
				if node.val-target < abs(result - target):
					result = node.val
				if node.left:
					node = node.left
				else:
					return result