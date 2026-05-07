class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        S=sum(nums)
        p=list(accumulate(nums))
        p.pop()

        return sum(2*x>=S for x in p)