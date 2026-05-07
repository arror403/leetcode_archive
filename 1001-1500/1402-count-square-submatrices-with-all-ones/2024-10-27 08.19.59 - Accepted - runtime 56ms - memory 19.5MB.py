class Solution:
    def countSquares(self, m: List[List[int]]) -> int:
        if not m or not m[0]: return 0

        r,c=len(m),len(m[0])
        dp=[[0]*c for _ in range(r)]
        res=0

        for i in range(r):
            for j in range(c):
                if m[i][j]:
                    # For cells in the first row or column, the largest square is itself
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        # Otherwise, use the DP relation to find the largest square submatrix
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                res+=dp[i][j]


        return res