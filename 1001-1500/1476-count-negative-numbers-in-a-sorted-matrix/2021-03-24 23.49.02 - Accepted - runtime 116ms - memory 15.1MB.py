class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        sum=0
        for r in grid:
            for c in r:
                if c<0:
                    sum+=1
                    
        return sum