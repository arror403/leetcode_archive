class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        m=(sorted(g) for _,g in groupby(nums, key=lambda x:x.bit_count()))

        return list(chain(*m))==sorted(nums)