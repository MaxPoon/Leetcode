# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def search(node):
	longest, currentAsc, currentDesc = 1, 1, 1
	leftLongest, leftAsc, leftDesc, rightLongest, rightAsc, rightDesc = 0, 0, 0, 0, 0, 0
	if node.left:
		leftLongest, leftAsc, leftDesc = search(node.left)
		if node.val == node.left.val+1:
			currentAsc = leftAsc+1
		if node.val == node.left.val-1:
			currentDesc = leftDesc+1
	if node.right:
		rightLongest, rightAsc, rightDesc = search(node.right)
		if node.val == node.right.val+1:
			currentAsc = max(currentAsc, rightAsc+1)
		if node.val == node.right.val-1:
			currentDesc = max(currentDesc, rightDesc+1)
	longest = max((longest, currentAsc, currentDesc, leftLongest, rightLongest))
	if node.left and node.right:
		if node.val == node.left.val+1 and node.val == node.right.val-1:
			longest = max(longest, leftAsc+rightDesc+1)
		if node.val == node.left.val-1 and node.val == node.right.val+1:
			longest = max(longest, leftDesc+rightAsc+1)
	return longest, currentAsc, currentDesc

class Solution(object):
	def longestConsecutive(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None: return 0        
		return search(root)[0]
