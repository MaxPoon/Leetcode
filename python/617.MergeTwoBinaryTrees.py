# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
		if not t1 and not t2: return None
		t = TreeNode(0)
		self.mergeRecursive(t1, t2, t)
		return t

	def mergeRecursive(self, node1, node2, node):
		if node1:
			node.val += node1.val
		if node2:
			node.val += node2.val
		node1Left = node1.left if node1 else None
		node1Right = node1.right if node1 else None
		node2Left = node2.left if node2 else None
		node2Right = node2.right if node2 else None
		if node1Left or node2Left:
			node.left = TreeNode(0)
			self.mergeRecursive(node1Left, node2Left, node.left)
		if node1Right or node2Right:
			node.right = TreeNode(0)
			self.mergeRecursive(node1Right, node2Right, node.right)
