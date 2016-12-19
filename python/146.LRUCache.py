class OrderNode(object):
	def __init__(self, key, val):
		self.val = val
		self.key = key
		self.prev = None
		self.next = None

class LRUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.capacity = capacity
		self.size = 0
		self.orderTable = {}
		self.head = None
		self.tail = None

	def get(self, key):
		"""
		:rtype: int
		"""
		if self.capacity == 0 or key not in self.orderTable: return -1
		if self.size==1 or self.head is self.orderTable[key]:
			return self.orderTable[key].val
		elif self.size == 2:
			self.head, self.tail = self.tail, self.head
			self.head.prev = self.head.next
			self.head.next = None
			self.tail.next = self.tail.prev
			self.tail.prev = None
			return self.orderTable[key].val
			
		if self.tail is self.orderTable[key]:
			self.orderTable[key].next.prev = None
			self.tail = self.orderTable[key].next
			self.orderTable[key].next = None
		else:
			self.orderTable[key].prev.next = self.orderTable[key].next
			self.orderTable[key].next.prev = self.orderTable[key].prev
		self.orderTable[key].prev = self.head
		self.head.next = self.orderTable[key]
		self.head = self.orderTable[key]
		return self.orderTable[key].val        
		

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""
		if self.capacity == 0:
			return 
		
		if key in self.orderTable:
			self.orderTable[key].val = value
			if self.size==1 or self.head is self.orderTable[key]: return
			if self.size == 2:
				self.head, self.tail = self.tail, self.head
				self.head.prev = self.head.next
				self.head.next = None
				self.tail.next = self.tail.prev
				self.tail.prev = None
				
			elif self.tail is self.orderTable[key]:
				self.orderTable[key].next.prev = None
				self.tail = self.orderTable[key].next
				self.orderTable[key].next = None
				self.orderTable[key].prev = self.head
				self.head.next = self.orderTable[key]
				self.head = self.orderTable[key]
			else:
				self.orderTable[key].prev.next = self.orderTable[key].next
				self.orderTable[key].next.prev = self.orderTable[key].prev
				self.orderTable[key].prev = self.head
				self.head.next = self.orderTable[key]
				self.head = self.orderTable[key]
			
			
		else:
			newNode = OrderNode(key, value)
			self.orderTable[key] = newNode
			if self.size == 0 :
				self.head = newNode
				self.tail = newNode
				self.size = 1
			elif self.capacity == 1:
				lruKey = self.tail.key
				del self.orderTable[lruKey]
				self.head = newNode
				self.tail = newNode
			
			elif self.size < self.capacity:
				newNode.prev = self.head
				self.head.next = newNode
				self.head = newNode
				self.size += 1
				if self.size == 2:
					self.tail.next = self.head
			else:
				lruKey = self.tail.key
				self.tail = self.tail.next
				self.tail.prev = None
				del self.orderTable[lruKey]
				newNode.prev = self.head
				self.head.next = newNode
				self.head = newNode