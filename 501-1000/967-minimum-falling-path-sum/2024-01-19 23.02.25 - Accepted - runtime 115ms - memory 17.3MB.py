class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        L=len(m)
        
        # Create a copy of the matrix to store the minimum falling path sum
        dp=[[0]*L for _ in range(L)]
        dp[0]=m[0]

        # Iterate over the remaining rows
        for r in range(1,L):
            for c in range(L):
                # Calculate the minimum falling path sum for the current cell
                dp[r][c]=m[r][c]+min(dp[r-1][c],dp[r-1][max(0,c-1)],dp[r-1][min(L-1,c+1)])
        # print(dp)
        return min(dp[-1])