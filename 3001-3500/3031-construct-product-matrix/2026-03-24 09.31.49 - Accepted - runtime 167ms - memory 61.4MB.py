class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        pre=[[0]*n for _ in range(m)]
        suf=[[0]*n for _ in range(m)]

        p=1
        for i in range(m):
            for j in range(n):
                pre[i][j]=p
                p=(p*grid[i][j])%12345

        p=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                suf[i][j]=p
                p=(p*grid[i][j])%12345

        
        return [[(pre[i][j]*suf[i][j])%12345 for j in range(n)] for i in range(m)]

        # TLE

        # m,n=len(grid),len(grid[0])
        # p=[[0]*n for _ in range(m)]
        # pre=[list(accumulate(r, operator.mul)) for r in grid]
        # suf=[list(accumulate(r[::-1], operator.mul))[::-1] for r in grid]

        # q=1
        # for r in grid:
        #     for c in r:
        #         q*=c
        
        # for i in range(m):
        #     for j in range(n):
        #         p[i][j]=(q//grid[i][j])%12345

        # return p