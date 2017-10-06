class Solution(object):
	def isValidSerialization(self, preorder):
		"""
		:type preorder: str
		:rtype: bool
		"""
		preorder = preorder.split(',')
		node = 0
		null = 0
		for i, c in enumerate(preorder):
			if c == '#':
				null += 1
				if i<len(preorder)-1 and null == node + 1:
					return False
			else:
				node += 1
		return null == node+1
