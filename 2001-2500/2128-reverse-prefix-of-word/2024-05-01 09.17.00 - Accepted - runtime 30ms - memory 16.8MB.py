class Solution:
    def reversePrefix(self, w: str, c: str) -> str:
        return w[:(i:=w.index(c)+1)][::-1]+w[i:] if c in w else w