class Solution:
    ##### improved by chatGPT #####
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r, c = len(land), len(land[0])
        res = []

        def DFS(row, col):
            if row >= r or col >= c or land[row][col] == 0:
                return [-1, -1]

            if land[row][col] == -1:
                return [-1, -1]

            # Mark the cell as visited
            land[row][col] = -1

            down = DFS(row + 1, col)
            right = DFS(row, col + 1)

            # Return the maximum row and column encountered
            return [max(row, down[0], right[0]), max(col, down[1], right[1])]

        for i in range(r):
            for j in range(c):
                if land[i][j] == 1:
                    bottom_row, right_col = DFS(i, j)
                    res.append([i, j, bottom_row, right_col])

        return res