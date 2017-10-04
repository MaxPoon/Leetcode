# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        self.length = length

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = randint(0, self.length-1)
        node = self.head
        while i:
            node = node.next
            i -= 1
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
