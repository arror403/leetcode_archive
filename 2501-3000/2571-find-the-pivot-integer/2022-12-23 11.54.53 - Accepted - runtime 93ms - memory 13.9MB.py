class Solution:
    def pivotInteger(self, n: int) -> int:
        x=n**2+n
        for i in range(1,n+1):
            if 2*(i**2)==x: return i
        return -1