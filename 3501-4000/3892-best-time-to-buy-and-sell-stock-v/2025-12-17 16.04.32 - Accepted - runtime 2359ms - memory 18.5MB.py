class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        cur = [[0,0,0] for _ in range(k+1)]
        Next = [[0,-inf,-inf] for _ in range(k+1)]

        for i in range(n-1, -1, -1):
            for j in range(k+1):
                for d in [0,1,2]:
                    take = -inf
                    dontTake = Next[j][d]

                    if j>0:
                        if d==1:
                            take = prices[i]+Next[j-1][0]
                        elif d==2:
                            take = -prices[i]+Next[j-1][0]
                        else:
                            take = max(prices[i]+Next[j][2], -prices[i]+Next[j][1])

                    cur[j][d] = max(take, dontTake)

            cur, Next = Next, cur


        return Next[k][0]