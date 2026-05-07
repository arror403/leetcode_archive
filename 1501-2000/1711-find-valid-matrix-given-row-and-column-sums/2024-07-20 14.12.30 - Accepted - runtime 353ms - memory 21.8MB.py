class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r,c=len(rowSum),len(colSum)
        res=[[0]*c for _ in range(r)]
        i,j=0,0
        
        while i<r and j<c:
            min_val=min(rowSum[i],colSum[j])

            res[i][j]=min_val
            rowSum[i]-=min_val
            colSum[j]-=min_val
            
            if rowSum[i]==0: i+=1
            if colSum[j]==0: j+=1
        

        return res