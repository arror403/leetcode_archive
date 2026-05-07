class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        L=len(s)
        s=list(s)

        for i in range(L//2):
            a,b=s[i],s[L-i-1]
            if a==b: continue
            elif a>b:
                s[i]=b
            else:
                s[L-i-1]=a

        return ''.join(s)