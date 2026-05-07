class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # return (time-1)%(2*(n))

        L=list(range(1,n+1))
        f=1
        while time>=n:
            time-=(n-1)
            f*=-1

        return L[time] if f==1 else L[time*f-1]