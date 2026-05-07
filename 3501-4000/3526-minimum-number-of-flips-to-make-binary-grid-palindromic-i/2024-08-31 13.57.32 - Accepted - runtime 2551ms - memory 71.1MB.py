class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        
        row_flips = sum(map(lambda r: sum(x^y for x,y in zip(r, r[::-1])), grid))
        col_flips = sum(map(lambda c: sum(x^y for x,y in zip(c, c[::-1])), zip(*grid)))
        
        return min(row_flips, col_flips)>>1