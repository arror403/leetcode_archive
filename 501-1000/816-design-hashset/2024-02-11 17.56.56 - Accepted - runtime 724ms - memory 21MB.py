class MyHashSet:

    def __init__(self):
        self.s=[]

    def add(self, key: int) -> None:
        if key not in self.s:
            self.s.append(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

    def contains(self, key: int) -> bool:
        # print(self.s)
        return key in self.s