class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            if 2*(i**2)==n**2+n: return i
        return -1