class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(dict.fromkeys(nums))<=2:return 0
        return len(nums)-nums.count(max(nums))-nums.count(min(nums))