class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res=0
        grid=[list(x) for x in zip(*grid)]
        print(grid)

        for c in grid:
            for i in range(len(c)-1):
                if (c[i+1]-c[i])<=0: 
                    res+=(c[i]-c[i+1]+1)
                    c[i+1]=c[i]+1


        return res