class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        L=len(s)-1
        for i in range(L, -1, -1):
            if s[i]!=' ':
                res+=1
            elif res>0:
                break
        return res