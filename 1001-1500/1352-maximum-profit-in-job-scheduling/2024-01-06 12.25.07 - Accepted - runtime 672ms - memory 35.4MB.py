class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        ##### power by Bing and chatGPT #####

        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [0] * (len(jobs) + 1)
        bs_cache = {}

        def binary_search(target):
            if target in bs_cache:
                return bs_cache[target]
            low, high = 0, len(jobs)
            while low < high:
                mid = (low + high) // 2
                if jobs[mid][1] <= target:
                    low = mid + 1
                else:
                    high = mid
            bs_cache[target] = low
            return low

        for i in range(1, len(jobs) + 1):
            j = binary_search(jobs[i - 1][0])
            dp[i] = max(dp[i - 1], jobs[i - 1][2] + dp[j])

        return dp[-1]