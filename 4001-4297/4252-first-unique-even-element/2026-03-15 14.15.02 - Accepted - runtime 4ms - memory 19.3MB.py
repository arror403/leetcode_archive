class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d=Counter(nums)

        for v in nums:
            if v%2==0 and d[v]==1:
                return v

        return -1