# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        p1,p2=head,head
        while True:
            if p2.next and p2.next.next:
                p2=p2.next.next
            else: return None
            p1 = p1.next
            if p1==p2: 
                p2=head
                while p2!=p1:
                    p2=p2.next
                    p1=p1.next
                return p1