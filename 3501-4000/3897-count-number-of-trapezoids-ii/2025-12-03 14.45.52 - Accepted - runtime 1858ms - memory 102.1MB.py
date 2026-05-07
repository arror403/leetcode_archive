class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = Counter()
        lines = Counter()
        mids = Counter()
        midlines = Counter()

        for (x1, y1), (x2, y2) in combinations(points, 2):
            dx = x2 - x1
            dy = y2 - y1
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g

            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy

            inter = dx * y1 - dy * x1
            slopes[dx, dy] += 1
            lines[dx, dy, inter] += 1
            mids[x1 + x2, y1 + y2] += 1
            midlines[x1 + x2, y1 + y2, dx, dy, inter] += 1

        res = sum(comb(v, 2) for v in slopes.values())
        res -= sum(comb(v, 2) for v in lines.values())
        res -= sum(comb(v, 2) for v in mids.values())
        res += sum(comb(v, 2) for v in midlines.values())


        return res

        
        # s=defaultdict(int)
        # v=defaultdict(int)

        # for a,b in combinations(points, 2):
        #     if b[0]==a[0]:
        #         v[a[0]]+=1
        #     else:
        #         m=(b[1]-a[1])/(b[0]-a[0])
        #         C=a[1]-m*a[0]
        #         s[(round(m,5),round(C,5))]+=1

        # # print(s,v)
        # r=defaultdict(list)        
        # for p,f in s.items():
        #     r[p[0]].append(f)

        # # print("r: ", r)
        # st=0
        # for x in r.values():
        #     if len(x)>1:
        #         S=sum(x)
        #         for i in x:
        #             st+=i*(S-i)
        # st//=2

        # vt=0
        # S=sum(v.values())
        # for i in v.values():
        #     vt+=i*(S-i)
        # vt//=2


        # return st+vt