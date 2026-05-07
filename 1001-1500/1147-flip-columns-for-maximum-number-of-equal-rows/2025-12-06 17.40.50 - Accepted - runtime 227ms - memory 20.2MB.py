class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = 0
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            cnt = 0
            flip = [1-c for c in matrix[i]]

            for k in range(i, m):
                if matrix[k] == matrix[i] or matrix[k] == flip: 
                    cnt+=1
            
            res = max(res, cnt)
        

        return res



        # m=set()
        # res=0
        # L=len(matrix[0])

        # for r in matrix:
        #     t=[]
        #     for c in r:
        #         t.append((c+1)%2)

        #     m.add(tuple(t))

        # for i,r in enumerate(matrix):
        #     s=sum(r)
        #     if s==(i+1) or (L-s)==(i+1):
        #         res+=1


        # return res