class Solution:
    def minOperations(self, s: str, k: int) -> int:
        def f(x,y): return (x+y-1)//y
        L = len(s)
        z = s.count('0')

        if L==k:
            return 0 if z==0 else (1 if z==L else -1)

        res = inf
        if z%2==0:
            m = max(f(z, k), f(z, L-k))
            m += m&1
            res = min(res, m)
        if z%2==k%2:
            m = max(f(z, k), f(L-z, L-k))
            m += m&1==0
            res = min(res, m)


        return res if res < inf else -1