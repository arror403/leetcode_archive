class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.m=grid
        self.l=len(grid)

    def adjacentSum(self, value: int) -> int:
        res=0
        for r in range(self.l):
            for c in range(self.l):
                if self.m[r][c]==value:
                    if r-1>=0: res+=self.m[r-1][c]
                    if r+1<self.l: res+=self.m[r+1][c]
                    if c-1>=0: res+=self.m[r][c-1]
                    if c+1<self.l: res+=self.m[r][c+1]
        return res

    def diagonalSum(self, value: int) -> int:
        res=0
        for r in range(self.l):
            for c in range(self.l):
                if self.m[r][c]==value:
                    if r-1>=0 and c-1>=0: res+=self.m[r-1][c-1]
                    if r+1<self.l and c+1<self.l: res+=self.m[r+1][c+1]
                    if r+1<self.l and c-1>=0: res+=self.m[r+1][c-1]
                    if r-1>=0 and c+1<self.l: res+=self.m[r-1][c+1]
        return res