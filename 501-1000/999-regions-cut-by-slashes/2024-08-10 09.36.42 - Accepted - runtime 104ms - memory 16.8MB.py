class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)
        uf=UnionFind(4*n*n)
        
        def index(row, col, i):
            return 4*(row*n + col) + i
        
        for row in range(n):
            for col in range(n):
                if row > 0:
                    uf.union(index(row, col, 0), index(row-1, col, 2))
                if col > 0:
                    uf.union(index(row, col, 3), index(row, col-1, 1))
                if grid[row][col] != '/':
                    uf.union(index(row, col, 0), index(row, col, 1))
                    uf.union(index(row, col, 2), index(row, col, 3))
                if grid[row][col] != '\\':
                    uf.union(index(row, col, 0), index(row, col, 3))
                    uf.union(index(row, col, 1), index(row, col, 2))
        
        return uf.count
        

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.count -= 1