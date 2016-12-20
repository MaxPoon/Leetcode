# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def plusOne(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		number = []
		node = head
		while node:
			number.append(node.val)
			node = node.next
		c = 1
		for i in range(len(number)-1, -1, -1):
			number[i]+=c
			c = int(number[i]>9)
			number[i] -= 10 if number[i]>9 else 0
		node = head
		i = 0
		while node:
			node.val = number[i]
			i+=1
			node = node.next
		if c==1:
			newNode = ListNode(1)
			newNode.next = head
			head = newNode
		return head