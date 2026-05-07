class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        S=sum(nums)
        p=list(accumulate(nums))


        return sum(p[i]>=(S-p[i]) for i in range(len(p)-1))