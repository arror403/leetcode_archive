class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        L=len(piles)
        dp=[[0]*(L+1) for _ in range(L+1)]
        p=list(accumulate(piles[::-1]))[::-1]+[0]

        for i in range(L+1): dp[i][L]=p[i]
        
        for i in range(L-1, -1, -1):
            for j in range(L-1, 0, -1):
                x=1
                while x<=j*2 and (x+i)<=L:
                    dp[i][j] = max(dp[i][j], p[i]-dp[i+x][max(j, x)])
                    x+=1


        return dp[0][1]