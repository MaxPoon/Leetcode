# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next: return head
		prevNode = None
		a = head
		b = a.next if a else None
		head = b
		while b:
			if prevNode:
				prevNode.next = b
			a.next = b.next
			b.next = a
			prevNode = a
			a = a.next
			b = a.next if a else None
		return head
