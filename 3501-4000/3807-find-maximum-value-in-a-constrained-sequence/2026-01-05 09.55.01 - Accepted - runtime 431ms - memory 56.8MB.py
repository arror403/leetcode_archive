class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        r = [float('inf')] * n

        for a, b in restrictions: r[a] = b
        
        for i in range(n-2, -1, -1):
            r[i] = min(r[i], r[i+1] + diff[i])
        
        r[0] = 0
        res = 0
        for i in range(1, n):
            r[i] = min(r[i], r[i - 1] + diff[i - 1])
            res = max(res, r[i])
        

        return res


        # l=[0]*n
        # r=[0]*n
        # for i,v in restrictions:
        #     l[i]=v
        #     r[i]=v

        # for i in range(1, n):
        #     d=abs(l[i]-l[i-1])
        #     if d<diff[i-1]:
        #         l[i] += diff[i-1]-d
        #     # r[n-i-1] += max(diff[n-i-2], abs(r[n-i-1]-r[n-i-2]))

        # print(l)

        # return 0