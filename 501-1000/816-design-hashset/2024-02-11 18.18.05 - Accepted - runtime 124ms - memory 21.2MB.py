class MyHashSet:
    def __init__(self):
        self.size = 1000  # Initial size of the hash table
        self.data = [[] for _ in range(self.size)]  # Use a list of lists for collision resolution

    def _hash(self, key):
        return key % self.size  # Simple hash function

    def add(self, key):
        index = self._hash(key)
        for item in self.data[index]:
            if item == key:
                return  # Key already exists
        self.data[index].append(key)

    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.data[index]):
            if item == key:
                del self.data[index][i]
                return

    def contains(self, key):
        index = self._hash(key)
        for item in self.data[index]:
            if item == key:
                return True
        return False