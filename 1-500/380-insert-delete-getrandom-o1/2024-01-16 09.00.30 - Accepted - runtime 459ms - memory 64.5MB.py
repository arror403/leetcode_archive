class RandomizedSet:

    def __init__(self):
        self.d=set()

    def insert(self, val: int) -> bool:
        if val not in self.d: 
            self.d.add(val)
            return True
        else: 
            return False


    def remove(self, val: int) -> bool:
        if val in self.d:
            self.d.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(list(self.d))