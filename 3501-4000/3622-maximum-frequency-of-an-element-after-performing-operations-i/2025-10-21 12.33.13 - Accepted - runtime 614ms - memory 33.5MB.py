class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        res = 0
        left = 0
        right = 0
        nums.sort()
        count = Counter(nums)

        # First pass: choose an existing number as the reference point
        for mid in range(n):
            # Adjust left pointer to keep nums[mid] - nums[left] within `k`
            while (nums[mid] - nums[left] > k):
                left+=1
            # Adjust right pointer to keep nums[right] - nums[mid] within `k`
            while (right < n-1 and nums[right+1]-nums[mid] <= k):
                right+=1
            # Calculate range size
            total = right - left + 1
            # Update ans with maximum achievable frequency for nums[mid] as the target
            res = max(res, min(total - count[nums[mid]], numOperations) + count[nums[mid]])

        # Second pass: choose a non-existent number as reference point
        left = 0
        for right in range(n):
            # Calculate hypothetical midpoint
            mid = (nums[left] + nums[right]) // 2
            # Adjust left pointer to ensure midpoint is within `k` range from both ends
            while (mid - nums[left] > k or nums[right] - mid > k):
                left+=1
                mid = (nums[left] + nums[right]) // 2
            # Update ans with maximum achievable frequency with the hypothetical midpoint
            res = max(res, min(right - left + 1, numOperations))


        return res