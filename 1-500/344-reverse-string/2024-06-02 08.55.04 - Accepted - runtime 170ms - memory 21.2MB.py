class Solution:
    def reverseString(self, s: List[str]) -> None:
        L=len(s)
        for i in range(L//2): s[i],s[L-i-1]=s[L-i-1],s[i]