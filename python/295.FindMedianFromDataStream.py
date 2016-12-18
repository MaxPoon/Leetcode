class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.leftAmount = 0
		self.rightAmount = 0

class MedianFinder:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = None
		self.size = 0

	def addNum(self, num):
		"""
		Adds a num into the data structure.
		:type num: int
		:rtype: void
		"""
		self.size += 1
		if self.root is None:
			self.root = Node(num)
		else:
			node = self.root
			while True:
				if num<=node.val:
					node.leftAmount += 1
					if node.left:
						node = node.left
					else:
						node.left = Node(num)
						return
				else:
					node.rightAmount += 1
					if node.right:
						node = node.right
					else:
						node.right = Node(num)
						return

	def findMedian(self):
		"""
		Returns the median of current data stream
		:rtype: float
		"""
		if self.size & 1==1:
			k = self.size//2+1
			median = self.findKth(k)
			return float(median)
		else:
			k1 = self.size>>1
			k2 = k1+1
			m1 = self.findKth(k1)
			m2 = self.findKth(k2)
			return (m1+m2)/2.0
				
	def findKth(self, k):
		node = self.root
		while True:
			if k<=node.leftAmount:
				node = node.left
			elif k == node.leftAmount + 1:
				return node.val
			else:
				k = k-node.leftAmount-1
				node = node.right
		
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()