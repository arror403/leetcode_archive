class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1])
        dp, dp2 = [[0, 0]], [[0, 0]]

        for _ in range(k):
            for s,e,v in events:
                i = bisect.bisect(dp, [s]) - 1
                if dp[i][1]+v > dp2[-1][1]:
                    dp2.append([e, dp[i][1] + v])

            dp, dp2 = dp2, [[0, 0]]


        return dp[-1][-1]