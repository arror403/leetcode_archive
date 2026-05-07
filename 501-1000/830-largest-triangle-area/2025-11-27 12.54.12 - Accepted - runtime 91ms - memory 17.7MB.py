class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        
        for p1, p2, p3 in combinations(points, 3):
            a = dist(p1, p2)
            b = dist(p2, p3)
            c = dist(p3, p1)
            
            s = (a+b+c)/2
            
            if s>a and s>b and s>c:
                area = sqrt(s*(s-a)*(s-b)*(s-c))
                res = max(res, area)
        

        return res