class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        L=len(piles)

        dp = [[0]*L for i in range(L)]
        for i in range(L): dp[i][i] = piles[i]
        for d in range(1, L):
            for i in range(L - d):
                dp[i][i+d] = max(piles[i] - dp[i+1][i+d], piles[i+d] - dp[i][i+d-1])

        print(dp)

        return dp[0][-1] > 0


        # def solve(x):
        #     d=deque(x)
        #     r=[0,0]
        #     t=0
        #     while d:
        #         if d[0]>d[-1]:
        #             r[t]+=d[0]
        #             d.popleft()
        #         elif d[0]<d[-1]:
        #             r[t]+=d[-1]
        #             d.pop()
        #         else:
        #             tmp=list(d)
        #             solve(tmp[1:])
        #             solve(tmp[:-1])

        #         t^=1

        #     return max(r[0], r[1])

        # res=solve(piles)

        # return res