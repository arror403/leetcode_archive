class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def canFormPairs(max_diff):
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    pairs += 1
                    i += 2  # Skip both elements
                else:
                    i += 1  # Try next element
            return pairs >= p
        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if canFormPairs(mid):
                right = mid
            else:
                left = mid + 1
                
                
        return left