class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_freq = 0
        total_operations = 0

        for right in range(len(nums)):
            total_operations += nums[right]

            while (right - left + 1) * nums[right] - total_operations > k:
                total_operations -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq