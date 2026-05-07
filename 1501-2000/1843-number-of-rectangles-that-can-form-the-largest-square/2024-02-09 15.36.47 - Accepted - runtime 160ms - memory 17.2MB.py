class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        t=[sorted(i) for i in rectangles]
        m=max(i[0] for i in t)
        return sum(1 for i in t if i[0]==m)