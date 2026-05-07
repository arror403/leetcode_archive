class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # return [sorted([[i,sum(v)] for i,v in enumerate(mat)], key=lambda x: x[1])[i][0] for i in range(k)]
        return [row[0] for row in sorted(enumerate(mat), key=lambda x: sum(x[1]))[:k]]