# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorder(node, k, nums):
	if node.left:
		inorder(node.left, k, nums)
	nums.append(node.val)
	if len(nums)>k:return
	if node.right:
		inorder(node.right,k, nums)
	

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		nums = []
		inorder(root, k, nums)
		return nums[k-1]