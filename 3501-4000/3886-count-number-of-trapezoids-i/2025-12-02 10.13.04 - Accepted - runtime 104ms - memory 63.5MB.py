class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d=defaultdict(int)
        MOD=(10**9+7)
        res=0

        for a,b in points: d[b]+=1

        # t=[(x*x-x)//2 for x in d.values()]

        # for p,q in combinations(t,2):
            # res+=(p*q)%(10**9+7) (a b c) ab bc ac (1/a + 1/b + 1/c) / abc

        total = 0
        for x in d.values():
            lines = x*(x-1)//2
            res = (res + total * lines) % MOD
            total = (total + lines) % MOD


        return res