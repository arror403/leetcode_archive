class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        d=[]
        for i,p in enumerate(points):
            if p[0]==x or p[1]==y:
                d.append([abs(x-p[0])+abs(y-p[1]),i])

        if not d: return -1

        m=min(x[0] for x in d)
        for v,i in d:
            if v==m: 
                return i