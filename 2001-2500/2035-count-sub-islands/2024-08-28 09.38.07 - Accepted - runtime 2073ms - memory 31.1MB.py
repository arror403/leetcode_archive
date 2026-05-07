class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n=len(grid2),len(grid2[0])
        return sum(self.dfs(grid1,grid2,i,j) for i in range(m) for j in range(n) if grid2[i][j])


    def dfs(self, B, A, i, j):
        m,n=len(A),len(A[0])
        if (i<0 or i==m or j<0 or j==n or A[i][j]==0): return 1
        res=1
        A[i][j]=0
        res &= self.dfs(B, A, i-1, j)
        res &= self.dfs(B, A, i+1, j)
        res &= self.dfs(B, A, i, j-1)
        res &= self.dfs(B, A, i, j+1)

        return res & B[i][j]