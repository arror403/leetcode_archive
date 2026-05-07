class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [sorted([[i,sum(v)] for i,v in enumerate(mat)], key=lambda x: x[1])[i][0] for i in range(k)]