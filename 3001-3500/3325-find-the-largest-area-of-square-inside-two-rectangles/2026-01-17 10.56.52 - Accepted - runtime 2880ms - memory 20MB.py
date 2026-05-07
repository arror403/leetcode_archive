class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        L = len(bottomLeft)
        res = 0

        for i in range(L):
            for j in range(i+1, L):
                minimum_x = max(bottomLeft[i][0], bottomLeft[j][0])
                maximum_x = min(topRight[i][0], topRight[j][0])
                minimum_y = max(bottomLeft[i][1], bottomLeft[j][1])
                maximum_y = min(topRight[i][1], topRight[j][1])
                
                if minimum_x < maximum_x and minimum_y < maximum_y:
                    s = min(maximum_x-minimum_x, maximum_y-minimum_y)
                    res = max(res, s**2)


        return res