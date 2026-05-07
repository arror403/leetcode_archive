class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={a:b for a,b in zip(order,"abcdefghijklmnopqrstuvwxyz")}

        return (x:=[''.join([d[c] for c in w]) for w in words])==sorted(x)