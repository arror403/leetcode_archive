class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [(1, -1)] * n  # (length, previous_index)
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i][0] < dp[j][0] + 1:
                    dp[i] = (dp[j][0] + 1, j)
            if dp[max_idx][0] < dp[i][0]:
                max_idx = i
        
        # Reconstruct result
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = dp[max_idx][1]
            

        return res[::-1]