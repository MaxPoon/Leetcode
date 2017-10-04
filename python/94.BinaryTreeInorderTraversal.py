# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        l = []
        self.inorder(root, l)
        return l
        
    def inorder(self, node, l):
        if node.left:
            self.inorder(node.left, l)
        l.append(node.val)
        if node.right:
            self.inorder(node.right, l)
