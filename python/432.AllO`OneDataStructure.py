class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.keysOrder = []
        self.keysPosition = {}
        self.deviation = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.keys:
            self.keys[key]+=1
            i = self.keysPosition[key]+self.deviation
            while(i<len(self.keysOrder)-1) and self.keys[self.keysOrder[i]] > self.keys[self.keysOrder[i+1]]:
                self.keysOrder[i], self.keysOrder[i+1] = self.keysOrder[i+1], self.keysOrder[i]
                self.keysPosition[self.keysOrder[i]]-=1
                i+=1
            self.keysPosition[key]=i-self.deviation
            
        else:
            self.keys[key] = 1
            self.keysOrder = [key] + self.keysOrder
            self.deviation += 1
            self.keysPosition[key] = -self.deviation

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.keys:
            if self.keys[key]==1:
                del self.keys[key]
                i = self.keysPosition[key]+self.deviation
                del self.keysPosition[key]
                for j in range(i):
                    self.keysPosition[self.keysOrder[j]]+=1
                self.keysOrder = self.keysOrder[:i]+self.keysOrder[i+1:]
                self.deviation -= 1
            else:
                self.keys[key]-=1
                i = self.keysPosition[key]+self.deviation
                while(i>0) and (self.keys[self.keysOrder[i]] < self.keys[self.keysOrder[i-1]]):
                    self.keysOrder[i], self.keysOrder[i-1] = self.keysOrder[i-1], self.keysOrder[i]
                    self.keysPosition[self.keysOrder[i]]+=1
                    i-=1
                self.keysPosition[key]=i-self.deviation
                
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.keysOrder):
            return self.keysOrder[-1]
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.keysOrder):
            return self.keysOrder[0]
        else:
            return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
