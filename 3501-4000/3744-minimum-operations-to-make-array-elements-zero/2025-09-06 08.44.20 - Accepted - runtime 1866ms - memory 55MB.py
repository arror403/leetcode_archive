class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res=0

        for a,b in queries:
            ops=0
            prev=1

            for d in range(1, 17):
                cur = prev * 4
                # Find the intersection between [start, end] and [prev, cur - 1]
                l=max(a, prev)
                r=min(b, cur-1)
                if r>=l:
                    ops+=(r-l+1)*d
                prev=cur
            # Since each operation can reduce two division steps, we need ceil(ops / 2) operations.
            res+=(ops+1)//2


        return res