class Solution:
    def subsetXORSum(self, m: List[int]) -> int:
        return sum(reduce(xor,i) for i in chain.from_iterable(combinations(m,r) for r in range(1,len(m)+1)))