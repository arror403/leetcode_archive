class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        S=sum(nums)
        p=list(accumulate(nums))
        p.pop()

        return sum(x>=(S-x) for x in p)