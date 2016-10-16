from random import choice
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.vals = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.vals.append(val)
        if val in self.index:
            self.index[val]+=[len(self.vals)-1]
            return False
        else:
            self.index[val] = [len(self.vals)-1]
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        i = self.index[val][0]
        self.index[val] = self.index[val][1:]
        tempK = len(self.vals)-1
        tempV = self.vals[tempK]
        self.vals[i], self.vals[len(self.vals)-1] =  self.vals[len(self.vals)-1], self.vals[i]
        self.vals.pop()
        for j in range(len(self.index[tempV])):
            if self.index[tempV][j] == tempK:
                self.index[tempV][j] = i
        if len(self.index[val]) == 0:
            del self.index[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
