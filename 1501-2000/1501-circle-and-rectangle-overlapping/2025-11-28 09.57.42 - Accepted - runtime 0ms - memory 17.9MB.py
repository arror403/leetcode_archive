class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # rx=range(x1,x2+1)
        # ry=range(y1,y2+1)

        # cx=range(xCenter-radius, xCenter+radius+1)
        # cy=range(yCenter-radius, yCenter+radius+1)

        # inter_x=set(rx)&set(cx)
        # if inter_x:
        #     for i in inter_x:
        #         if yCenter-sqrt(radius**2-(xCenter-i)**2)<=w
        def f(i, j, k):
            if i <= k <= j:
                return 0
            return i - k if k < i else k - j

        a = f(x1, x2, xCenter)
        b = f(y1, y2, yCenter)
        return a**2 + b**2 <= radius**2