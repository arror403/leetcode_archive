class RandomizedSet:

    def __init__(self):
        self.x=[]
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.data_map:
            self.x.append(val)
            self.data_map[val] = len(self.x) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data_map:
            idx, last = self.data_map[val], self.x[-1]
            self.x[idx], self.data_map[last] = last, idx
            self.x.pop(); self.data_map.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.x)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()