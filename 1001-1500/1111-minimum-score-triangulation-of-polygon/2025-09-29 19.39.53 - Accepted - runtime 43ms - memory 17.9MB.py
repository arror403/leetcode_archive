class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # values.sort()
        # res=values[0]*values[1]

        # return sum([res*x for x in values[2:]])

        dp = [[0]*50 for _ in range(50)]
        L = len(values)

        for i in range(L-1, -1, -1):
            for j in range(i+1, L):
                k=i+1
                while k<j:
                    if dp[i][j]==0: dp[i][j]=inf
                    dp[i][j] = min(dp[i][j], dp[i][k] + values[i]*values[j]*values[k] + dp[k][j])
                    k+=1


        return dp[0][L-1]