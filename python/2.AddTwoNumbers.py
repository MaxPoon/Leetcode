# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        r = ListNode((n1.val+n2.val)%10)
        rNode = r
        c = (n1.val+n2.val)//10
        while (n1.next or n2.next or c):
            v1,v2 =0,0
            if(n1.next):
                v1 = n1.next.val
                n1 = n1.next
            if(n2.next):
                v2 = n2.next.val
                n2 = n2.next
            temp = ListNode((v1+v2+c)%10)
            c = (v1+v2+c)//10
            rNode.next = temp
            rNode = temp
        return r