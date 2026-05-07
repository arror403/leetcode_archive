class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        dp = [1] * n  # Initialize all elements to 1

        # Create a dictionary to store the index of each element for quick lookup
        index = {v:i for i,v in enumerate(arr)}
        # print((index))

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    # If arr[j] is a valid factor of arr[i]
                    k = arr[i] // arr[j]
                    if k in index:
                        # Update dp[i] by multiplying the number of trees at dp[j] and dp[k]
                        dp[i] += dp[j] * dp[index[k]]
                        dp[i] %= MOD

        # Sum up all the values in the dp array to get the total number of binary trees
        return sum(dp) % MOD