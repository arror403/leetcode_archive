class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res=list(combinations(characters,combinationLength))
        self.i=0

    def next(self) -> str:
        tmp=self.res[self.i]
        self.i+=1
        return "".join(tmp)

    def hasNext(self) -> bool:
        self.l=len(self.res)
        return self.i < self.l


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()