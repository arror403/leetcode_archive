class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        while nums != sorted(nums):
            minSum = inf
            p = -1

            for i in range(len(nums) - 1):
                if (nums[i] + nums[i + 1]) < minSum:
                    minSum = nums[i] + nums[i + 1]
                    p = i

            nums[p] += nums[p + 1]
            del nums[p + 1]
            res += 1
        

        return res