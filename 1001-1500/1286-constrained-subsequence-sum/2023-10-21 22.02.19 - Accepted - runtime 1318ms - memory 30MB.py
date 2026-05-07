class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # dp[i] represents the maximum subsequence sum ending at index i
        dp = [0] * n
        
        # Initialize a deque (double-ended queue) to keep track of the maximum values in the window
        max_values = deque()
        
        for i in range(n):
            # Remove values that are out of the current window of size k
            while max_values and max_values[0] < (i-k):
                max_values.popleft()
            
            # Calculate the maximum subsequence sum ending at index i by taking the maximum value from the previous window and adding the current element, or just using the current element if the previous window's maximum is negative.
            
            dp[i] = max(nums[i], nums[i] + (dp[max_values[0]] if max_values else 0))
            
            # Remove values from the back of the deque that are smaller than the current maximum
            while max_values and dp[i] >= dp[max_values[-1]]:
                max_values.pop()
            
            max_values.append(i)
        
        # Return the maximum subsequence sum among all indices
        return max(dp)