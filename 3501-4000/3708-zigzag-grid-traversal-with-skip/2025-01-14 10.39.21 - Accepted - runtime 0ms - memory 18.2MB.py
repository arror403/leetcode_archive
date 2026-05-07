class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res=[]

        for i,r in enumerate(grid):
            if i%2==0:
                res.append(r[::2])
            else:
                r=r[1::2]
                res.append(r[::-1])


        return list(chain.from_iterable(res))