# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

	def __init__(self, nestedList):
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
		self.pointers = [0] if len(nestedList) > 0 else []
		self.stack = [nestedList] if len(nestedList) > 0 else []
		

	def next(self):
		"""
		:rtype: int
		"""
		self.pointers[-1]+=1
		return self.stack[-1][self.pointers[-1]-1].getInteger()

	def hasNext(self):
		"""
		:rtype: bool
		"""
		while len(self.pointers):
			if self.pointers[-1] >= len(self.stack[-1]):
				self.pointers.pop()
				self.stack.pop()
				continue
			if self.stack[-1][self.pointers[-1]].isInteger():
				return True
			else:
				newList = self.stack[-1][self.pointers[-1]].getList()
				if len(newList):
					self.stack.append(newList)
					self.pointers[-1]+=1
					self.pointers.append(0)
				else:
					self.pointers[-1] += 1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())