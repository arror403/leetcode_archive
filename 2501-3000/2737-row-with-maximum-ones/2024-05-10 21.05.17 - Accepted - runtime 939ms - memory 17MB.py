class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return next([i,sum(r)] for i,r in enumerate(mat) if sum(r)==max(sum(i) for i in mat))