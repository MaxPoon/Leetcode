# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, longest = self.findLongest(root)
        return longest

    def findLongest(self, node):
        if not node: return 0, 0
        maxLeft, maxLeftLen = self.findLongest(node.left)
        maxRight, maxRightLen = self.findLongest(node.right)
        maxThis = 0
        if node.left and node.val == node.left.val:
            maxThis = maxLeft + 1
        if node.right and node.val == node.right.val:
            maxThis = max(maxThis, maxRight+1)
        maxThisLen = max(maxLeftLen, maxRightLen)
        if node.left and node.right and node.val == node.left.val and node.val == node.right.val:
            maxThisLen = max(maxThisLen, maxLeft + maxRight + 2)
        elif node.left and node.val == node.left.val:
            maxThisLen = max(maxThisLen, maxLeft + 1)
        elif node.right and node.val == node.right.val:
            maxThisLen = max(maxThisLen, maxRight + 1)
        return maxThis, maxThisLen
