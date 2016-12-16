def search(node, longest, currentLength):
	if currentLength > longest : longest = currentLength
	if node.left:
		if node.left.val == node.val + 1:
			longest = max(longest, search(node.left, longest, currentLength+1))
		else:
			longest = max(longest, search(node.left, longest, 1))
	if node.right:
		if node.right.val == node.val + 1:
			longest = max(longest, search(node.right, longest, currentLength+1))
		else:
			longest = max(longest, search(node.right, longest, 1))
	return longest

class Solution(object):
	def longestConsecutive(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None: return 0
		return search(root, 1, 1)