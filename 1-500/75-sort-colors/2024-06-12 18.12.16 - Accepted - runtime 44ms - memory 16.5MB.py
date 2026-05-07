class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:]=chain.from_iterable(Counter(nums)[i]*[i] for i in [0,1,2])