# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findPaths(node, currentPath, paths):
	if node.left:
		currentPath.append(str(node.val))
		findPaths(node.left, currentPath, paths)
		currentPath.pop()
	if node.right:
		currentPath.append(str(node.val))
		findPaths(node.right, currentPath, paths)
		currentPath.pop()
	if not node.left and not node.right:
		currentPath.append(str(node.val))
		paths.append("->".join(currentPath))
		currentPath.pop()

class Solution(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		if not root: return []
		paths = []
		currentPath = []
		findPaths(root, currentPath, paths)
		return paths
