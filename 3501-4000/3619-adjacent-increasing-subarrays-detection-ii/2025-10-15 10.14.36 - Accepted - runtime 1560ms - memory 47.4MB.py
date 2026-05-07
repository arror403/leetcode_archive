class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        L = len(nums)

        # Step 1: Compute length of sorted runs STARTING at i (backward pass)
        run_from = [0] * L
        run_from[L - 1] = 1
        for i in range(L - 2, -1, -1):
            if nums[i] < nums[i+1]:
                run_from[i] = 1 + run_from[i+1]
            else:
                run_from[i] = 1
                
        # Step 2: Compute length of sorted runs ENDING at i (forward pass)
        run_to = [0] * L
        run_to[0] = 1
        for i in range(1, L):
            if nums[i] > nums[i-1]:
                run_to[i] = 1 + run_to[i-1]
            else:
                run_to[i] = 1

        # Step 3: Find the best junction (single pass)
        max_k = 0
        # A junction is between i-1 and i
        for i in range(1, L):
            # Max length of the first block ending at i-1
            len1 = run_to[i-1]
            # Max length of the second block starting at i
            len2 = run_from[i]
            
            # The common length k can be at most the minimum of the two
            k = min(len1, len2)
            
            if k > max_k:
                max_k = k
                

        return max_k