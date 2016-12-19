class OrderNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        self.called = 1

class LFUCache(object):

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
        :type key: int
        :rtype: int
        """
        if self.capacity == 0: return -1
        if key not in self.orderTable: return -1
        self.orderTable[key].called += 1
        self.update(key)
        return self.orderTable[key].val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0 : return
        if key in self.orderTable:
            self.orderTable[key].val = value
            self.orderTable[key].called += 1
            self.update(key)
        else:
            newNode = OrderNode(key, value)
            self.orderTable[key] = newNode
            if self.size==self.capacity:
                self.delete()
            if self.size == 0:
                self.head = newNode
                self.tail = newNode
                self.size = 1
                return
            else:
                self.size += 1
                self.tail.prev = newNode
                newNode.next = self.tail
                self.tail = newNode
                self.update(key)
        
    def delete(self):
        self.size -= 1
        key = self.tail.key
        self.tail = self.tail.next
        if self.tail:
            self.tail.prev = None
        if self.head is self.orderTable[key]: self.head = None
        del self.orderTable[key]
        
    def update(self, key):
        if self.tail is self.orderTable[key] and self.orderTable[key].next and self.orderTable[key].called >= self.orderTable[key].next.called:
            self.tail = self.tail.next
        while self.orderTable[key].next and self.orderTable[key].called >= self.orderTable[key].next.called:
            key2 = self.orderTable[key].next.key
            self.orderTable[key].next = self.orderTable[key2].next
            self.orderTable[key2].prev = self.orderTable[key].prev
            if self.orderTable[key2].next:
                self.orderTable[key2].next.prev = self.orderTable[key]
            if self.orderTable[key].prev:
                self.orderTable[key].prev.next = self.orderTable[key2]
            self.orderTable[key].prev = self.orderTable[key2]
            self.orderTable[key2].next = self.orderTable[key]
        if self.orderTable[key].next is None:
            self.head = self.orderTable[key]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)