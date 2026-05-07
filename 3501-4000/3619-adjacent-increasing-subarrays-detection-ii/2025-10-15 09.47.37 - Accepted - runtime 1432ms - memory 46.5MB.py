class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        L = len(nums)

        # Step 1: Pre-compute sorted runs (O(L))
        sorted_run = [0] * L
        sorted_run[L - 1] = 1
        for i in range(L - 2, -1, -1):
            if nums[i] < nums[i+1]:
                sorted_run[i] = 1 + sorted_run[i+1]
            else:
                sorted_run[i] = 1

        # Step 2: Define the check function for our binary search
        def check(k: int) -> bool:
            """Checks if a solution of size k exists in O(L) time."""
            if k == 0:
                return True
            # We need to find an 'i' such that a sorted run of length k
            # starts at 'i' AND another one starts at 'i+k'.
            for i in range(L - 2 * k + 1):
                if sorted_run[i] >= k and sorted_run[i+k] >= k:
                    return True
            return False

        # Step 3: Binary search for the largest k (O(log L) checks * O(L) per check)
        low, high = 0, L // 2
        ans = 0
        while low <= high:
            k = (low + high) // 2
            if check(k):
                ans = k      # This k is possible, try for a larger one
                low = k + 1
            else:
                high = k - 1 # This k is not possible, try a smaller one
                

        return ans



        # L = len(nums)

        # # Step 1: Compute length of sorted runs STARTING at i (backward pass)
        # run_from = [0] * L
        # run_from[L - 1] = 1
        # for i in range(L - 2, -1, -1):
        #     if nums[i] < nums[i+1]:
        #         run_from[i] = 1 + run_from[i+1]
        #     else:
        #         run_from[i] = 1
                
        # # Step 2: Compute length of sorted runs ENDING at i (forward pass)
        # run_to = [0] * L
        # run_to[0] = 1
        # for i in range(1, L):
        #     if nums[i] > nums[i-1]:
        #         run_to[i] = 1 + run_to[i-1]
        #     else:
        #         run_to[i] = 1

        # # Step 3: Find the best junction (single pass)
        # max_k = 0
        # # A junction is between i-1 and i
        # for i in range(1, L):
        #     # Max length of the first block ending at i-1
        #     len1 = run_to[i-1]
        #     # Max length of the second block starting at i
        #     len2 = run_from[i]
            
        #     # The common length k can be at most the minimum of the two
        #     k = min(len1, len2)
            
        #     if k > max_k:
        #         max_k = k
                

        # return max_k