# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def searchLongestPath(node):
            if not node:
                return 0, 0
            leftLongest, leftDiameter = searchLongestPath(node.left)
            rightLongest, rightDiameter = searchLongestPath(node.right)
            diameter = max(max(leftDiameter, rightDiameter), leftLongest+rightLongest)
            return max(leftLongest, rightLongest)+1, diameter
        _, diameter = searchLongestPath(root)
        return diameter
