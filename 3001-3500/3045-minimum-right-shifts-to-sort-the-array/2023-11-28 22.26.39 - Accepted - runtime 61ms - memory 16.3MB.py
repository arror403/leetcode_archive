class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        b=sorted(nums)
        res=0
        for _ in range(len(nums)):
            if nums==b: return res
            else:
                nums=nums[-1:]+nums[:-1]
                res+=1

        return -1