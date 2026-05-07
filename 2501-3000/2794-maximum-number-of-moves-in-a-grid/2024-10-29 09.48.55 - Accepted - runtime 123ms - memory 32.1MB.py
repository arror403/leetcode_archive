class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        res=0
        m,n=len(grid),len(grid[0])
        dirs=[[0,1], [1,1], [-1,1]]
        cache=[[-1]*n for _ in range(m)]

        def dp(i, j):
            if (cache[i][j] != -1): return cache[i][j]
            ans=0
            for x,y in dirs:
                ni = i + x
                nj = j + y
                if (ni>=0 and ni<m and nj<n and grid[i][j]<grid[ni][nj]):
                    ans=max(ans, 1 + dp(ni, nj))

            cache[i][j] = ans

            return ans

        for i in range(m): res=max(res, dp(i, 0))


        return res