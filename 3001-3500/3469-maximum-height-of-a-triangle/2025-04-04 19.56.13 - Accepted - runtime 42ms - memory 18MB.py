class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        even=[2, 6, 12, 20, 30, 42, 56, 72, 90]
        odd=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

        s1r=bisect.bisect_right(even, red)
        s1b=bisect.bisect_right(odd, blue)

        s2r=bisect.bisect_right(odd, red)
        s2b=bisect.bisect_right(even, blue)

        height1 = min(2*s1r, 2*s1b-1) if s1b > 0 else 0
        height2 = min(2*s2r-1, 2*s2b) if s2r > 0 else 0
        
        
        return max(height1, height2)+1