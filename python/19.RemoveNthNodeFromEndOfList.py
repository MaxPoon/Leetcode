# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        L = []
        while(node):
            L.append(node)
            node=node.next
        if n==len(L):
            return head.next
        elif n==1:
            node = L[len(L)-2]
            node.next = None
        else:
            node = L[len(L)-n-1]
            node.next = node.next.next
        return head
