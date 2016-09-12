# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not(node.left or node.right):
                return [node.val, 0]
            elif not node.left:
                right = dfs(node.right)
                return [node.val+right[1], max(right)]
            elif not node.right:
                left = dfs(node.left)
                return [node.val+left[1], max(left)]
            right = dfs(node.right)
            left = dfs(node.left)
            return [node.val+right[1]+left[1], max(right)+max(left)]
        if root == None:
            return 0
        return max(dfs(root))
