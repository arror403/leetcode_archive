class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def line_len(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

        d = 0
        for a, b, c in combinations(points, 3):
            p, q, r = line_len(a, b), line_len(a, c), line_len(b, c)
            S = (p+q+r)/2
            if (S<p or S<q or S<r): continue
            d = max(d, (S*(S-p)*(S-q)*(S-r))**(1/2))


        return d