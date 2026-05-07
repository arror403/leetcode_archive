class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(subgrid):
            # Check if subgrid contains numbers 1-9
            if set(sum(subgrid,[]))!=set(range(1,10)): return 0
            # Check rows, columns, and diagonals
            target_sum=sum(subgrid[0])
            # Check rows
            if any(sum(row)!=target_sum for row in subgrid): return 0
            # Check columns
            if any(sum(subgrid[i][j] for i in range(3))!=target_sum for j in range(3)): return 0
            # Check diagonals
            if sum(subgrid[i][i] for i in range(3))!=target_sum: return 0
            if sum(subgrid[i][2-i] for i in range(3))!=target_sum: return 0
            
            return 1


        res=0
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if is_magic_square([grid[x][j:j+3] for x in range(i, i+3)]): res+=1
        
        return res