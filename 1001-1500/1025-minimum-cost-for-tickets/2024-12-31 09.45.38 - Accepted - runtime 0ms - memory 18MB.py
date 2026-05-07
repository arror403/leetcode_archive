class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel=set(days)
        dp=[0]*30

        for i in range(days[0], days[-1]+1):
            # If not a travel day, copy value from previous day
            if i not in travel:
                dp[i%30]=dp[(i-1)%30]
            else:
                dp[i%30]=min(dp[(i-1)%30]+costs[0],         # 1. Buy 1-day pass
                            dp[max(0,i-7)%30]+costs[1],     # 2. Buy 7-day pass
                            dp[max(0,i-30)%30]+costs[2])    # 3. Buy 30-day pass


        return dp[days[-1]%30]