class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(index):
            # Base case: if we've covered all days
            if index >= len(days): return 0
            # Get the current day
            current_day = days[index]
            # Try 1-day pass
            cost1 = costs[0] + dp(index + 1)
            # Try 7-day pass: find the first day beyond current_day + 6
            i = index
            while i < len(days) and days[i] < current_day + 7: i += 1
            cost7 = costs[1] + dp(i)
            # Try 30-day pass: find the first day beyond current_day + 29
            i = index
            while i < len(days) and days[i] < current_day + 30: i += 1
            cost30 = costs[2] + dp(i)
            # Return minimum of all three options
            return min(cost1, cost7, cost30)
        

        return dp(0)

        # travel=days
        # # unordered_set<int> travel(begin(days), end(days))
        # dp=[0]*30
        # # int dp[30] = {}
        # for i in range(len(days)):
        #     if travel[i]==travel[-1]:
        #         dp[i%30]=dp[(i-1)%30]
        #     else:
        #         dp[i%30]=min(dp[(i-1)%30]+costs[0], dp[max(0, i-7)%30]+costs[1], dp[max(0, i-30)%30]+costs[2])


        # return dp[days[-1]%30]

        # # for (int i = days.front(); i <= days.back(); ++i)
        # #     if (travel.find(i) == travel.end()) dp[i % 30] = dp[(i - 1) % 30]
        # #     else dp[i % 30] = min({ dp[(i - 1) % 30] + costs[0],
        # #         dp[max(0, i - 7) % 30] + costs[1], dp[max(0, i - 30) % 30] + costs[2] })
        # # return dp[days.back() % 30]