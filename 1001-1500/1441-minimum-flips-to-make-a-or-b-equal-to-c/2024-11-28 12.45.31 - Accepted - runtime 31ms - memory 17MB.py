class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        L = max(len(a), len(b), len(c))
        a, b, c = a.zfill(L), b.zfill(L), c.zfill(L)
        res = 0

        for i in range(L):
            if c[i]=='0':
                res+=(int(a[i])+int(b[i]))
            else:
                if a[i]==b[i]=='0':
                    res+=1


        return res