class Solution:
    def passThePillow(self, n: int, t: int) -> int:
        return list(range(1,n+1))[(t%(n-1)) if (t//(n-1))%2==0 else -((t%(n-1))+1)]
