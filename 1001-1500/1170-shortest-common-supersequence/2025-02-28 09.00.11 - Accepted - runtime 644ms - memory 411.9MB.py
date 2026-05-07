class Solution:
    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        def lcs(A, B):
            n=len(A)
            m=len(B)
            dp=[["" for _ in range(m+1)] for d in range(n+1)]
            # vector<vector<string>> dp(n + 1, vector<string>(m + 1, ""))
            for i in range(n):
                for j in range(m):
                    if A[i]==B[j]:
                        dp[i+1][j+1]=dp[i][j]+A[i]
                    else:
                        dp[i+1][j+1]=dp[i+1][j] if len(dp[i+1][j])>len(dp[i][j+1]) else dp[i][j+1]

            return dp[n][m]

        i=j=0
        res=""
        
        for c in lcs(A, B):
            while A[i]!=c:
                res+=A[i]
                i+=1
            while B[j]!=c:
                res+=B[j]
                j+=1

            res+=c
            i+=1
            j+=1
        

        return res+A[i:]+B[j:]