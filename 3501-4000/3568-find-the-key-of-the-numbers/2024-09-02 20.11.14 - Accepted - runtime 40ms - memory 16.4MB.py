class Solution:
    def generateKey(self, a: int, b: int, c: int) -> int:
        a,b,c=str(a).zfill(4),str(b).zfill(4),str(c).zfill(4)

        return int(''.join(min(a[i],b[i],c[i]) for i in range(4)))