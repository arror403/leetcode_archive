class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_freq = 0
        operations = 0

        for right in range(len(nums)):
            operations += (nums[right] - nums[right - 1]) * (right - left)

            while operations > k:
                operations -= nums[right] - nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq