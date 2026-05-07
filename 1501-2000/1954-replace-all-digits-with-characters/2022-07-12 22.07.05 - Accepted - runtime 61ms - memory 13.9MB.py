class Solution:
    def replaceDigits(self, s: str) -> str:
        t=""
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            if i%2==0:
                t+=s[i]
            else:
                t+=alpha[ord(s[i-1])-97+int(s[i])]
        return t