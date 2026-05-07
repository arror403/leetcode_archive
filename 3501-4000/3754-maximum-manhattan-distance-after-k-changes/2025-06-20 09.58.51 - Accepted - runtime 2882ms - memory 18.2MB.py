class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # d={'N':(0,1), 'E':(1,0), 'W':(-1,0), 'S':(0,-1)}
        res=0

        for diag in [{"N", "E"}, {"N", "W"}, {"S", "E"}, {"S", "W"}]:
            cur_k, dist = k, 0
            for c in s:
                if (c in diag) or cur_k:
                    dist+=1
                    cur_k-=(0 if c in diag else 1)
                else:
                    dist-=1

                res=max(res, dist)


        return res