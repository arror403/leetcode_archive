class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        ##### power by chatGPT #####


        if not nums: return []

        n = len(nums)
        dp = [1] * n  # Initialize an array to store the length of the longest increasing subsequence

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Find the maximum length of increasing subsequence
        max_length = max(dp)

        # Reconstruct the subsequence
        result = []
        current_length = max_length
        for i in range(n - 1, -1, -1):
            if dp[i] == current_length:
                result.append(nums[i])
                current_length -= 1

        return len(result[::-1])