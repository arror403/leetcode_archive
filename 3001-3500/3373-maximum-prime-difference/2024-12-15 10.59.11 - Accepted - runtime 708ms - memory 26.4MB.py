class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        a=next(i for i,v in enumerate(nums) if v in p)
        b=next(i for i,v in enumerate(reversed(nums)) if v in p)

        return len(nums)-(b+a+1)