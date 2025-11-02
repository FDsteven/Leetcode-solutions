from random import choice
class RandomizedSet(object):
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx],self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.list)
    
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]