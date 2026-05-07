class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        L=len(nums)+1
        p=chain.from_iterable(combinations(nums,r) for r in range(L))

        return sum(reduce(lambda x,y:x^y, i) for i in p if i)