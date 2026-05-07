class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return reduce(xor, (v for v,f in Counter(nums).items() if f==2), 0)