class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m*n) != len(original): return []

        res=[]
        L=len(original)//m

        for i in range(m):
            res.append(original[i*L:i*L+n])

        return res