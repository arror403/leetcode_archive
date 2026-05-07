class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        r1=[ax1,ax2,bx1,bx2]    
        r2=[ay1,ay2,by1,by2]
        r1.sort()
        r2.sort()
        # print(r1,r2)
        if self.isRectangleOverlap([ax1,ay1,ax2,ay2], [bx1,by1,bx2,by2]):
            return abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))-abs((r1[1]-r1[2])*(r2[1]-r2[2]))
        else:
            return abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))

    def isRectangleOverlap(self, rec1, rec2):
        widthIsPositive = min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])
        heightIsPositive = min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
        return ( widthIsPositive and heightIsPositive)


