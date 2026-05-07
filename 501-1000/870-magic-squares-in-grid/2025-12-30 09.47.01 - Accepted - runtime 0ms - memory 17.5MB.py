class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # Early exit if grid is too small
        if R < 3 or C < 3: return 0
        
        res = 0
        # Iterate through all possible top-left corners of 3x3 grids
        for i in range(R - 2):
            for j in range(C - 2):
                if grid[i+1][j+1] != 5: continue
                
                a, b, c = grid[i][j],     grid[i][j+1],     grid[i][j+2]
                d,    e = grid[i+1][j],                     grid[i+1][j+2]
                f, g, h = grid[i+2][j],   grid[i+2][j+1],   grid[i+2][j+2]
                
                if {a, b, c, d, e, f, g, h} != {1, 2, 3, 4, 6, 7, 8, 9}: continue
                
                # Check Sums (Target is always 15)
                # Since center is 5, diagonals and cross-lines must sum to 10 (pairs around 5)
                # a b c
                # d 5 e
                # f g h
                if (a + h == 10 and
                    c + f == 10 and
                    b + g == 10 and
                    d + e == 10 and
                    a + b + c == 15 and
                    a + d + f == 15):
                    res += 1
                    
                    
        return res