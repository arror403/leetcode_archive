import numpy as np

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        ##### power by chatGPT #####

        res = np.zeros((m, n), dtype=int)

        for ri, ci in indices:
            res[ri, :] += 1  # Increment entire row
            res[:, ci] += 1  # Increment entire column

        b = np.sum(res % 2 == 1)

        return b
