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

class Solution(object):
	def depthSum(self, nestedList):
		"""
		:type nestedList: List[NestedInteger]
		:rtype: int
		"""
		return self.solve(nestedList, 1)

	def solve(self, nestedList, level):
		total = 0
		for element in nestedList:
			if element.isInteger():
				total += element.getInteger()*level
			else:
				total += self.solve(element.getList(), level+1)
		return total
