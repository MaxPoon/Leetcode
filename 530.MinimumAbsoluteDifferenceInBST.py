# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		l = []
		self.inOrder(root, l)
		return min(abs(a-b) for a, b in zip(l[:-1], l[1:]))
		
	def inOrder(self, node, l):
		if node.left:
			self.inOrder(node.left, l)
		l.append(node.val)
		if node.right:
			self.inOrder(node.right, l)
