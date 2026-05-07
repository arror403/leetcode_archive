class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        t=set()
        for i in range(len(s)-k+1):
            t.add(s[i:i+k])

        return len(t)==2**k