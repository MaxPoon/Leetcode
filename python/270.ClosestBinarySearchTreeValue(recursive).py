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
		if root.val == target: return root.val
		if (target < root.val and not root.left) or (target > root.val and not root.right):
			return root.val
		if target < root.val:
			closestInLeft = self.closestValue(root.left, target)
			if abs(closestInLeft - target) < abs(root.val-target):
				return closestInLeft
			return root.val
		else:
			closestInRight = self.closestValue(root.right, target)
			if abs(closestInRight - target) < abs(root.val-target):
				return closestInRight
			return root.val
