class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [] if m*n!=(L:=len(original)) else [original[i*L//m:i*L//m+n] for i in range(m)]