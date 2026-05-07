class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp=[[-1]*301 for _ in range(301)]

        @lru_cache(maxsize=None)
        def f(n, p):
            if n<0: return 0
            if n==0: return 1
            if p**x>n: return 0
            if dp[n][p]!=-1: return dp[n][p]
            
            pick=f(n-p**x, p+1)
            skip=f(n, p+1)

            dp[n][p]=(skip+pick)%(10**9+7)
            
            return dp[n][p]


        return f(n, 1)