# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def traverse(node, x, depth, orderTable):
	if x not in orderTable:
		orderTable[x] = []
	orderTable[x].append((node.val, depth))
	if node.left:
		traverse(node.left, x-1, depth+1, orderTable)
	if node.right:
		traverse(node.right, x+1, depth+1, orderTable)

class Solution(object):
	def verticalOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root: return []
		orderTable = {}
		traverse(root, 0, 0, orderTable)
		for v in orderTable.values():
			v.sort(key=lambda x: x[1])
		result = []
		for k in sorted(orderTable.keys()):
			result.append(list(map(lambda x: x[0], orderTable[k])))
		return result