class Solution:
    def soupServings(self, n: int) -> float:
        if n>4800: return 1

        d={}
        def f(a, b):
            nonlocal d

            if (a,b) in d: return d[a,b]
            if a<=0 and b<=0: return 0.5
            if a<=0: return 1
            if b<=0: return 0

            d[(a,b)]=0.25*(f(a-4, b)+f(a-3, b-1)+f(a-2, b-2)+f(a-1, b-3))

            return d[(a,b)]
        
        n=ceil(n/25)
        

        return f(n, n)