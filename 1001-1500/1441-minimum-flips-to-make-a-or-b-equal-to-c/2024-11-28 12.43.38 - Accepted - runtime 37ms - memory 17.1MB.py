class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        L = len(bin(max(a, b, c))) - 2
        a, b, c = bin(a)[2:].zfill(L), bin(b)[2:].zfill(L), bin(c)[2:].zfill(L)
        res = 0

        for i in range(L):
            if c[i]=='0':
                res+=(int(a[i])+int(b[i]))
            elif a[i]==b[i]=='0':
                res+=1


        return res