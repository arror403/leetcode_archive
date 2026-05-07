class Solution:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W:
            return 1.0

        dp = [0.0] * (N + 1)
        dp[0] = 1.0

        window_sum = 1.0
        probability = 0.0

        for i in range(1, N + 1):
            dp[i] = window_sum / W
            if i < K:
                window_sum += dp[i]
            else:
                probability += dp[i]

            if i - W >= 0:
                window_sum -= dp[i - W]

        return probability