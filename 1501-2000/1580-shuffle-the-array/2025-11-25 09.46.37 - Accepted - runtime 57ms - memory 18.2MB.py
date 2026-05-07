class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        L=len(nums)//2
        return chain.from_iterable(zip(nums[:L],nums[L:]))