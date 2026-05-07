class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r,c=len(rowSum),len(colSum)
        res=[[0]*c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        
        
        return res