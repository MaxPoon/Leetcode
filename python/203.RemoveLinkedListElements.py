# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		prev = None
		newHead = None
		node = head
		while node:
			if node.val != val:
				if prev:
					prev.next = node
					prev = node
				else:
					newHead = node
					prev = node
			if not node.next: break
			node = node.next
		if prev:
			prev.next = None
		return newHead
