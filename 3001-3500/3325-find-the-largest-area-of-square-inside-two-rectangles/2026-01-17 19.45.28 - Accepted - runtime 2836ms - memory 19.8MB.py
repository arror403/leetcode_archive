class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        L = len(bottomLeft)
        res = 0

        for i in range(L):
            for j in range(i+1, L):
                # Left edge of overlap = rightmost of the two left edges
                minimum_x = max(bottomLeft[i][0], bottomLeft[j][0])
                # Right edge of overlap = leftmost of the two right edges
                maximum_x = min(topRight[i][0], topRight[j][0])
                # Bottom edge of overlap = topmost of the two bottom edges
                minimum_y = max(bottomLeft[i][1], bottomLeft[j][1])
                # Top edge of overlap = bottommost of the two top edges
                maximum_y = min(topRight[i][1], topRight[j][1])
                # Overlap exists only if left < right AND bottom < top
                if minimum_x < maximum_x and minimum_y < maximum_y:
                    # Calculate the side length of the largest square that fits in the overlap
                    # The square side is limited by the smaller dimension (width or height)
                    s = min(maximum_x - minimum_x, maximum_y - minimum_y)
                    res = max(res, s ** 2)


        return res