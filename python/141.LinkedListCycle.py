# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        p1=head
        p2=head.next
        while True:
            if p2.next and p2.next.next:
                p2=p2.next.next
            else: return False
            p1 = p1.next
            if p1==p2: return True