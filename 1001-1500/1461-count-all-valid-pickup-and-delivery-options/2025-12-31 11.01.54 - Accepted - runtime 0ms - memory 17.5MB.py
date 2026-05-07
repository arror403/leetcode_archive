class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
 
        for i in range(2, n+1):
            x = i*2
            res *= x*(x-1)//2


        return res%(10**9 + 7)