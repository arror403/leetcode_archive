class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # x=[p[0] for p in points]
        # y=[p[1] for p in points]
        # Mx,mx=max(x),min(x)
        # My,my=max(y),min(y)

        # A=[(Mx-mx)*abs(My), (Mx-mx)*abs(my), (My-my)*abs(Mx), (My-my)*abs(mx)]

        # return max(A)/2

        return max(abs(i[0]*j[1]+j[0]*k[1]+k[0]*i[1]-j[0]*i[1]-k[0]*j[1]-i[0]*k[1]) for i,j,k in combinations(points,3))/2