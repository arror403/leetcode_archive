class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=0
        F=False
        for f in Counter(s).values():
            if f%2==0:
                res+=f
            else:
                F=True
                res+=f-1
        

        return res+1 if F else res