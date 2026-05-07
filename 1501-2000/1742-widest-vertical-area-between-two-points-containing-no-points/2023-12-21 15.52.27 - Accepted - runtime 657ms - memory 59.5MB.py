class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        t=sorted([i[0] for i in points])
        return max([t[i] - t[i-1] for i in range(1,len(points))])
         