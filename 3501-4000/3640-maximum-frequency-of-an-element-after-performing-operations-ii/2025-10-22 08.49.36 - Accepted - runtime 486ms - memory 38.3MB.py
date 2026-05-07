class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        res = 0
        left = 0
        right = 0
        nums.sort()
        count = Counter(nums)

        for mid in range(n):
            while (nums[mid] - nums[left] > k):
                left+=1
            while (right < n-1 and nums[right+1]-nums[mid] <= k):
                right+=1
            total = right - left + 1
            res = max(res, min(total - count[nums[mid]], numOperations) + count[nums[mid]])

        left = 0
        for right in range(n):
            mid = (nums[left] + nums[right]) // 2
            while (mid - nums[left] > k or nums[right] - mid > k):
                left+=1
                mid = (nums[left] + nums[right]) // 2
            res = max(res, min(right - left + 1, numOperations))


        return res