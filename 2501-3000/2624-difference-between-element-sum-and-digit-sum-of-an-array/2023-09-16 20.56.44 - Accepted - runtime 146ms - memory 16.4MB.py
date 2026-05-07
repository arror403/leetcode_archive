class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums)-sum([j for i in nums for j in list(map(int,str(i)))]))