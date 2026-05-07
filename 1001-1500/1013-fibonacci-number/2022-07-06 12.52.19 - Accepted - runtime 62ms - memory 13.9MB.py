class Solution:
    def fib(self, n: int) -> int:
        b=[0,1]
        if n==0: return 0
        elif n==1: return 1
        else:
            for i in range(2,n+1):
                b.append(b[i-1]+b[i-2])

            return b[-1]    