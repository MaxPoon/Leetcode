from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.items:
            return False
        else:
            self.items[val]=True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.items:
            del self.items[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        k = self.items.keys()
        if len(k)==0:
            return False
        r = randint(0,len(k)-1)
        return k[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
