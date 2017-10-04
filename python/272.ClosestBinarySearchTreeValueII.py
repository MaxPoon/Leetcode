# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from heapq import heappush, heappop
class Solution(object):
	def closestKValues(self, root, target, k):
		"""
		:type root: TreeNode
		:type target: float
		:type k: int
		:rtype: List[int]
		"""
		heap = []
		self.closestRecursive(root, target, heap, k)
		return [closest[1] for closest in heap]
		
	def closestRecursive(self, node, target, heap, k):
		diff = abs(node.val - target)
		if len(heap) < k:
			heappush(heap, (-diff, node.val))
		elif diff < -heap[0][0]:
			heappop(heap)
			heappush(heap, (-diff, node.val))
		if node.left and (len(heap)<k or diff < -heap[0][0] or node.val >= target):
			self.closestRecursive(node.left, target, heap, k)
		if node.right and (len(heap)<k or diff < -heap[0][0] or node.val<=target):
			self.closestRecursive(node.right, target, heap, k)
