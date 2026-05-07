class Solution:
    def minRemoval(self, A: List[int], k: int) -> int:
        A.sort()
        L=len(A)
        return min([L-bisect_right(A, A[i]*k)+i for i in range(L)]+[L-1])