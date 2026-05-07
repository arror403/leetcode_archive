class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        ##### power by chatGPT #####

        min_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            # Calculate the maximum difference between corresponding coordinates
            min_time += max(abs(x2 - x1), abs(y2 - y1))

        return min_time