class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(l, r, m, q):
            if l > r:  dp(r, l, m, q)
            if l == r: res.add(q)
            
            for i in range(1, l + 1):
                for j in range(l-i+1, r-i+1):
                    if not (m+1)//2 >= i + j >= l + r - m//2: continue
                    dp(i, j, (m + 1) // 2, q + 1)
        
        res = set()
        dp(firstPlayer, n - secondPlayer + 1, n, 1)


        return [min(res), max(res)]