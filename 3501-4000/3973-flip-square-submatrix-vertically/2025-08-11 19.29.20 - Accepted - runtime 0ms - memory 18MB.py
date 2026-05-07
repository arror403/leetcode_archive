class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        tmp=[grid[r][y:y+k] for r in range(x, x+k)][::-1]

        for i in range(x, x+k):
            for j in range(y, y+k):
                grid[i][j]=tmp[i-x][j-y]


        return grid