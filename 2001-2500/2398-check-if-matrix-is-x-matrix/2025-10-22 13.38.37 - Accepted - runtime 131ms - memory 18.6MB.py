class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        s = [(i, i) for i in range(n)] + [(i, n-i-1) for i in range(n)]
        # left_to_right = [(i, i) for i in range(n)]
        # right_to_left = [(i, n-i-1) for i in range(n)]

        for i in range(n):
            for j in range(n):
                if (i, j) in s:
                    if grid[i][j]==0:
                        return False
                elif grid[i][j]:
                    return False

        return True