class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        L = len(nums)
        nums.sort()

        for i in range(L - 2):
            k = i + 2
            for j in range(i + 1 , L - 1):
                if nums[i] == 0: break
                while k < L and nums[i] + nums[j] > nums[k]: k += 1
                res += k - j - 1


        return res