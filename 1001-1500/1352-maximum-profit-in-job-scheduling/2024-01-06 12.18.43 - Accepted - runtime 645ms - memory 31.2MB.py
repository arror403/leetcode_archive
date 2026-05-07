class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        ##### power by Bing and chatGPT #####

        t = [list(i) for i in zip(startTime, endTime, profit)]
        t.sort(key=lambda x: x[1])

        def binary_search(arr, target):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid][1] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Initialize the DP table
        dp = [0] * (len(t) + 1)

        # Fill the DP table
        for i in range(1, len(t) + 1):
            # Find the index of the last non-overlapping job using binary search
            j = binary_search(t, t[i - 1][0])

            # Update the DP table
            dp[i] = max(dp[i - 1], t[i - 1][2] + dp[j])

        return dp[-1]