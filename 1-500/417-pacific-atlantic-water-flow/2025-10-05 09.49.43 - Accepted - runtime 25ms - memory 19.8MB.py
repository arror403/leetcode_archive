class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = set()
        r, c = len(matrix), len(matrix[0])
        pacific = [[0]*c for _ in range(r)]
        atlantic = [[0]*c for _ in range(r)]

        def dfs(visited, height, x, y):
            if (x<0 or x>=r or y<0 or y>=c or visited[x][y] or matrix[x][y]<height):
                return
            visited[x][y] = True
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(visited, matrix[x][y], x+a, y+b)


        for i in range(r):
            dfs(pacific, -inf, i, 0)
            dfs(atlantic, -inf, i, c-1)

        for i in range(c):
            dfs(pacific, -inf, 0, i)
            dfs(atlantic, -inf, r-1, i)

        for i in range(r):
            for j in range(c):
                if pacific[i][j] and atlantic[i][j]:
                    res.add((i, j))


        return [list(p) for p in res]