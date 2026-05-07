class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        s=defaultdict(int)
        v=defaultdict(int)

        for a,b in combinations(points, 2):
            if b[0]==a[0]:
                v[a[0]]+=1
            else:
                m=(b[1]-a[1])/(b[0]-a[0])
                C=a[1]-m*a[0]
                s[(round(m,5),round(C,5))]+=1

        r = max(max(s.values(), default=0), max(v.values(), default=0))
        # print(s,v,r)
        return int((sqrt(8*r+1)+1)/2)