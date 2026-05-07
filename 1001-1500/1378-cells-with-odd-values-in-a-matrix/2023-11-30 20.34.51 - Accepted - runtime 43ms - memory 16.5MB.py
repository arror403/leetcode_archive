class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res=[[0]*n for _ in range(m)]
        b=0
        for ri,ci in indices:

            for r in res:
                r[ci] += 1

            for i in range(n):
                res[ri][i] += 1
                
        for r in res:
            for c in r:
                if c%2==1: b+=1
        # print(res)
        return b