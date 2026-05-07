class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [-1,-1] if target not in nums else [nums.index(target), len(nums)-nums[::-1].index(target)-1]

        # return [i for i,v in enumerate(nums) if v==target] or [-1,-1]