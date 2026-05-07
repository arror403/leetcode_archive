class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        def countOneRow(A):
            res = length = 0

            for i in range(len(A)):
                length=0 if A[i]==0 else length+1
                res+=length

            return res


        m,n=len(mat),len(mat[0])
        res = 0

        for up in range(m):
            h=[1]*n
            for down in range(up, m):
                for k in range(n):
                    if mat[down][k]==0: h[k]=0
                        
                res+=countOneRow(h)


        return res