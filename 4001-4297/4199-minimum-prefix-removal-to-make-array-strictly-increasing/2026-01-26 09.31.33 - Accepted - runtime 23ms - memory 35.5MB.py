class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        nums=nums[::-1]
        L=len(nums)
        for i in range(L-1):
            if nums[i+1]>=nums[i]:
                return L-i-1

        return 0