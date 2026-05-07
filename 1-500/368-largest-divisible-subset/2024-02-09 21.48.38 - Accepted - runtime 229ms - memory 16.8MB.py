class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        ##### power by chatGPT #####

        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_length, max_index = 1, 0

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if dp[i] > max_length:
                max_length = dp[i]
                max_index = i

        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result[::-1]