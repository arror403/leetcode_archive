class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        ##### power by chatGPT #####

        row_counts = [0] * m
        col_counts = [0] * n

        for ri, ci in indices:
            row_counts[ri] += 1
            col_counts[ci] += 1

        b = 0
        for ri in range(m):
            for ci in range(n):
                count = row_counts[ri] + col_counts[ci]
                if count % 2 == 1:
                    b += 1

        return b