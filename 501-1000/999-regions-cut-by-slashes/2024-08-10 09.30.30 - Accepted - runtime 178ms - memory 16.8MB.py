class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Check if a cell is within bounds and unvisited
        def isValidCell(row, col):
            nonlocal expandedGrid
            n=len(expandedGrid)
            return row>=0 and col>=0 and row<n and col<n and expandedGrid[row][col]==0


        # Flood fill algorithm to mark all cells in a region
        def floodFill(row, col):
            nonlocal expandedGrid
            DIRECTIONS=[[0,1],[0,-1],[1,0],[-1,0]]
            q=deque()
            expandedGrid[row][col]=1
            q.append([row,col])

            while q:
                currentRow,currentCol=q[0]
                q.popleft()
                # Check all four directions from the current cell
                for direction in DIRECTIONS:
                    newRow=direction[0]+currentRow
                    newCol=direction[1]+currentCol
                    # If the new cell is valid and unvisited, mark it and add to queue
                    if isValidCell(newRow, newCol):
                        expandedGrid[newRow][newCol]=1
                        q.append([newRow, newCol])


        gridSize=len(grid)
        # Create a 3x3 matrix for each cell in the original grid
        expandedGrid=[[0]*3*gridSize for _ in range(3*gridSize)]

        # Populate the expanded grid based on the original grid
        # 1 represents a barrier in the expanded grid
        for i in range(gridSize):
            for j in range(gridSize):
                baseRow=i*3
                baseCol=j*3
                # Check the character in the original grid
                if (grid[i][j]=="\\"):
                    # Mark diagonal for backslash
                    expandedGrid[baseRow][baseCol]=1
                    expandedGrid[baseRow+1][baseCol+1]=1
                    expandedGrid[baseRow+2][baseCol+2]=1
                elif (grid[i][j]=='/'):
                    # Mark diagonal for forward slash
                    expandedGrid[baseRow][baseCol+2]=1
                    expandedGrid[baseRow+1][baseCol+1]=1
                    expandedGrid[baseRow+2][baseCol]=1

        regionCount=0
        # Count regions using flood fill
        for i in range(gridSize*3):
            for j in range(gridSize*3):
                # If we find an unvisited cell (0), it's a new region
                if expandedGrid[i][j]==0:
                    # Fill that region
                    floodFill(i,j)
                    regionCount+=1


        return regionCount