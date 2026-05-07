class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pf=[0]+list(accumulate(arr, operator.xor))
        return [pf[l]^pf[r+1] for l,r in queries]