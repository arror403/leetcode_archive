class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        p=[[0]*n for _ in range(m)]
        pL=[[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='X':
                    p[i][j]=1
                    pL[i][j]=True
                if grid[i][j]=='Y':
                    p[i][j]=-1
                    pL[i][j]=True

        pr=[list(accumulate(r)) for r in p]
        pc=[list(accumulate(c)) for c in zip(*pr)]
        prL=[list(accumulate(r, operator.or_)) for r in pL]
        pcL=[list(accumulate(c, operator.or_)) for c in zip(*prL)]

        res=0
        for i in range(n):
            for j in range(m):
                if pc[i][j]==0 and pcL[i][j]:
                    res+=1


        return res


# [["X","Y","."],
#  [".",".","."],
#  ["Y",".","X"],
#  ["X","Y","."]]

# [(1, 0, 0), 
#  (1, 0, 0), 
#  (0, -1, 0), 
#  (1, -1, 0)]



# [[".","."],
#  ["Y","X"]]

# [(0, 0), 
#  (-1, 0)]

# [(False, False), 
#  (True, True)]