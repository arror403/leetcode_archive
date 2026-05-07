class Solution:
    def canSortArray(self, A: List[int]) -> bool:
        return list(chain.from_iterable(sorted(g) for _,g in groupby(A,key=lambda x:x.bit_count())))==sorted(A)