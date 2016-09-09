# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            if not (l1 or l2):
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            n1 = l1
            n2 = l2
            l = ListNode(min(n1.val,n2.val))
            n = l
            while(n1 or n2):
                if n1.val<n2.val:
                    n1 = n1.next
                else:
                    n2 = n2.next
                if n1 == None:
                    n.next = n2
                    return l
                if n2 == None:
                    n.next = n1
                    return l
                n.next = ListNode(min(n1.val,n2.val))
                n = n.next

        if len(lists) == 0:
            return None
        elif len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        elif len(lists) == 1:
            return lists[0]
        else:
            length = len(lists)
            return self.mergeKLists([self.mergeKLists(lists[:length/2]),self.mergeKLists(lists[length/2:])])
