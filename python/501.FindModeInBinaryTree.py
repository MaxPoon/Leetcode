# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root is None: return []
		mode = []
		occurence = 0
		currentElement = None
		currentOccurence = -1
		mode, occurence, currentElement, currentOccurence =\
				self.inOrder(root, mode, occurence, currentElement, currentOccurence)
		if currentOccurence == occurence and (not mode or mode[-1]!=currentElement):
			mode.append(currentElement)
		if currentOccurence > occurence:
			mode = [currentElement]
			occurence = currentOccurence
		return mode
		
	def inOrder(self, node, mode, occurence, currentElement, currentOccurence):
		if node.left:
			mode, occurence, currentElement, currentOccurence =\
				self.inOrder(node.left, mode, occurence, currentElement, currentOccurence)
		if currentOccurence == occurence and (not mode or mode[-1]!=currentElement):
			mode.append(currentElement)
		if currentOccurence > occurence:
			mode = [currentElement]
			occurence = currentOccurence
		if currentElement == node.val:
			currentOccurence += 1
		else:
			currentElement = node.val
			currentOccurence = 1
		if node.right:
			mode, occurence, currentElement, currentOccurence =\
				self.inOrder(node.right, mode, occurence, currentElement, currentOccurence)
		return mode, occurence, currentElement, currentOccurence
