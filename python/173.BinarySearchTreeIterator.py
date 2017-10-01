# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.stack = []
		self.node = root
		while self.node and self.node.left:
			self.stack.append(self.node)
			self.node = self.node.left
		if self.node:
			self.stack.append(self.node)
			self.node = None

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return (self.node and self.node.right) or self.stack

	def next(self):
		"""
		:rtype: int
		"""
		if not self.hasNext(): return None
		if self.node and self.node.right:
			self.node = self.node.right
		elif self.stack:
			self.node = self.stack.pop()
			return self.node.val
		while self.node.left:
			self.stack.append(self.node)
			self.node = self.node.left
		return self.node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())