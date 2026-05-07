class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
        def isOverlap(r1, r2):
            return min(r1[2], r2[2]) > max(r1[0], r2[0]) and min(r1[3], r2[3]) > max(r1[1], r2[1])

        A=abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))

        if isOverlap([ax1,ay1,ax2,ay2], [bx1,by1,bx2,by2]):
            r1=sorted([ax1,ax2,bx1,bx2])
            r2=sorted([ay1,ay2,by1,by2])
            return A-abs((r1[1]-r1[2])*(r2[1]-r2[2]))
        else:
            return A