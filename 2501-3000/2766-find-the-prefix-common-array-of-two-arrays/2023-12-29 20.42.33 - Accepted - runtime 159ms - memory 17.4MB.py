class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        L=len(A)
        res = [0]*L
        a = set()
        b = set()
        common = set()

        for i in range(L):
            a.add(A[i])
            b.add(B[i])

            if A[i] in b: common.add(A[i])
            if B[i] in a: common.add(B[i])

            res[i] = len(common)
        
        return res