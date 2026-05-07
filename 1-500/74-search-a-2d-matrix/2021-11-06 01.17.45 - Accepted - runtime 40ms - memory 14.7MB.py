class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R=0
        for r in matrix:
            for c in r:
                if c==target:
                    R=1
                    break
            if R==1:
                break
        return R