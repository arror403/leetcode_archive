class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c=Counter(map(lambda x:x%2, nums))
        return c[0]>1