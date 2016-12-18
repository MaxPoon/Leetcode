# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.
		:type root: TreeNode
		:rtype: str
		"""
		string = ""
		nodes = [root]
		while nodes:
			node = nodes.pop(0)
			if node is None:
				string+="None#"
			else:
				string += str(node.val)+"#"
				nodes.append(node.left)
				nodes.append(node.right)
		return string
		

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		:type data: str
		:rtype: TreeNode
		"""
		i = 0
		val = ""
		nodes = []
		j = -1
		while i<len(data):
			if data[i]!="#":
				val+=data[i]
			else:
				if val != "None":
					val = int(val)
				if val=="None":
					node = None
				else:
					node = TreeNode(val)
				if j==-1 and val == "None": return None
				if j!= -1:
					parent = nodes[j//2]
					if j&1==0:
						parent.left = node
					else:
						parent.right = node
				j += 1
				if node is not None:
					nodes.append(node)
				val = ""
			i+=1
		return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))