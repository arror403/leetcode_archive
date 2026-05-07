class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l=len(mat[0])
        sum=0
        for i in range(l): sum+=mat[i][i]
        
        for i in range(l-1,-1,-1):
            if (l-i-1)!=i:
                sum+=mat[l-i-1][i]

        return sum