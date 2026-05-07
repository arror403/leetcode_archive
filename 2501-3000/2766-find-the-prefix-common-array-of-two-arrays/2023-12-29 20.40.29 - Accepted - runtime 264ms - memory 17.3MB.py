class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # return [len(set(A[:i]) & set(B[:i])) for i in range(1,len(A)+1)]
        L=len(A)
        a,b=set(),set()
        res=[]

        for i in range(L):
            a.add(A[i])
            b.add(B[i])
            res.append(len(a&b))

        return res
                    