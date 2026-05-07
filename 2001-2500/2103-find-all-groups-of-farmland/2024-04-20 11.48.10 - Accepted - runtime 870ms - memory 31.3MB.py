class Solution:
    # improved by Copilot
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r,c=len(land),len(land[0])
        res=[]
        visited=[[False for _ in range(c)] for _ in range(r)]

        def DFS(row, col):
            if row>=r or col>=c or visited[row][col] or land[row][col]==0:
                return [row-1, col-1]

            # Mark the cell as visited
            visited[row][col]=True

            down=DFS(row+1, col)
            right=DFS(row, col+1)

            # Return the maximum row and column encountered
            return [max(down[0], right[0]), max(down[1], right[1])]


        for i,R in enumerate(land):
            for j,C in enumerate(R):
                if C==1 and not visited[i][j]:
                    res.append([i,j]+DFS(i,j))

        return res