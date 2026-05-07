class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir=[-1,0,1,0,-1]
        m,n=len(grid),len(grid[0])
        fresh=0
        res=-1
        q=deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
                    
        while q:
            size=len(q)
            for _ in range(size):
                p=q.popleft()
                for i in range(4):
                    r=p[0]+dir[i]
                    c=p[1]+dir[i+1]
                    if r>=0 and r<m and c>=0 and c<n and grid[r][c]==1:
                        grid[r][c]=2
                        q.append([r,c])
                        fresh-=1
            res+=1
        
        if fresh>0: return -1
        if res==-1: return 0

        return res