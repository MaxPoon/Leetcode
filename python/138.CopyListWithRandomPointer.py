# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        clonedHead = RandomListNode(head.label)
        nodeMap = {head.label: clonedHead}
        node = head
        clonedNode = clonedHead
        while node.next:
            clonedNode.next = RandomListNode(node.next.label)
            clonedNode = clonedNode.next
            node = node.next
            nodeMap[clonedNode.label] = clonedNode
        node = head
        while node:
            if node.random:
                nodeMap[node.label].random = nodeMap[node.random.label]
            node = node.next
        return clonedHead
