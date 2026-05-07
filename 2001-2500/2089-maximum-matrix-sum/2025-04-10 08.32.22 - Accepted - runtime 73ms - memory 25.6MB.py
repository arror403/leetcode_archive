class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_cnt=res=0
        L=len(matrix)
        m=inf

        for i in range(L):
            for j in range(L):
                res+=abs(matrix[i][j])

                if matrix[i][j]<0: neg_cnt+=1

                if m>=abs(matrix[i][j]): m=abs(matrix[i][j])

        
        return res if neg_cnt%2==0 else res-2*m