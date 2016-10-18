# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseOneList(self, head, tail,after):
        currentNode = after
        nextNode = head
        while(currentNode!=tail):
            temp = nextNode.next
            nextNode.next = currentNode
            currentNode = nextNode
            nextNode = temp
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None: return None
        if k==1: return head
        n=1
        start = head
        node = start.next
        beforeHead = ListNode(0)
        beforeHead.next = head
        lastEnd = beforeHead
        while(node):
            n+=1
            if n==k:
                temp = node.next
                self.reverseOneList(start, node, temp)
                lastEnd.next = node
                lastEnd = start
                node = temp
                start = node
                n=0
            else:
                node = node.next
        return beforeHead.next
