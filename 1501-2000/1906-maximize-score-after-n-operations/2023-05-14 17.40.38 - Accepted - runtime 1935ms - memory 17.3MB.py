class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (1 << n) for _ in range(n // 2 + 1)]
        # dp[i][mask] represents the maximum score that can be obtained after i operations
        # and selecting the numbers represented by the mask
        
        # pre-calculate the GCD between each pair of numbers in nums
        gcd = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                gcd[i][j] = gcd[j][i] = math.gcd(nums[i], nums[j])
        
        # iterate over all possible masks and operations
        for i in range(1, n // 2 + 1):
            for mask in range(1, 1 << n):
                if bin(mask).count("1") == 2 * i:
                    # try all possible pairs of numbers represented by the mask
                    for j in range(n):
                        if mask & (1 << j):
                            for k in range(j+1, n):
                                if mask & (1 << k):
                                    # update the maximum score
                                    dp[i][mask] = max(dp[i][mask], dp[i-1][mask ^ (1 << j) ^ (1 << k)] + i * gcd[j][k])
        return dp[n//2][(1<<n)-1]