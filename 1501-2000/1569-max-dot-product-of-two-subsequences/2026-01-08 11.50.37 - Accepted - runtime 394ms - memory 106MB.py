class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(maxsize = None)
        def solve(i, j):
            if i < 0 or j < 0: return float('-inf')

            use_current = nums1[i] * nums2[j] + max(solve(i - 1, j - 1), 0)
            skip_nums1 = solve(i - 1, j)
            skip_nums2 = solve(i, j - 1)
            
            return max(use_current, skip_nums1, skip_nums2)


        return solve(len(nums1) - 1, len(nums2) - 1)