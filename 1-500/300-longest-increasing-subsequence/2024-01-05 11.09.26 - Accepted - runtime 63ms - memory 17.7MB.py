class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        ##### power by chatGPT #####


        tails = [0] * len(nums)
        size = 0

        for num in nums:
            left, right = 0, size

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            tails[left] = num
            size = max(size, left + 1)

        return size