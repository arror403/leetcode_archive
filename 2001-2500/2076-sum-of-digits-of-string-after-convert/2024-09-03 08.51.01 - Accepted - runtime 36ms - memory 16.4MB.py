class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t=""
        for c in s: t+=str(ord(c)-96)
        for _ in range(k): t=sum(int(d) for d in str(t))
        
        return t