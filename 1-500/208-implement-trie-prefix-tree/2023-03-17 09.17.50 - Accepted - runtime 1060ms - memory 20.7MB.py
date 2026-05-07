class Trie:

    def __init__(self):
        self.m=[]

    def insert(self, word: str) -> None:
        self.m.append(word)

    def search(self, word: str) -> bool:
        return word in self.m 

    def startsWith(self, prefix: str) -> bool:
        for i in self.m:
            if i.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)