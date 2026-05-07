class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        lr,lc=len(matrix),len(matrix[0])
        m=[]

        for c in list(zip(*matrix)):
            p=[1 if c[0] else 0]+[0]*(lr-1)
            for i in range(1, lr):
                if c[i]:
                    if p[i-1]:
                        p[i]=p[i-1]+1
                    else:
                        p[i]=1
            m.append(p)

        m=list(zip(*m))

        res=0
        for r in m:
            tmp=sorted(r)
            for j in range(1, lc+1):
                res = max(res, j * tmp[lc - j])


        return res