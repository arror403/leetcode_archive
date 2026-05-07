class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        return sorted([[(x**2+y**2)**(0.5), x*y] for x,y in d], key=lambda t:(t[0],t[1]))[-1][1]