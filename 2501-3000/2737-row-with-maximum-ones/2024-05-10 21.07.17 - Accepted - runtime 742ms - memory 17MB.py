class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        r_sum=[sum(i) for i in mat]
        M=max(r_sum)
        return next([i,v] for i,v in enumerate(r_sum) if v==M)