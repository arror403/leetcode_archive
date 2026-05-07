class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if (len(points) == 0): return 0

        # Arrays.sort(points, (a, b) -> a[1] - b[1])
        points=sorted(points, key = lambda x : x[1])


        arrowPos = points[0][1]
        arrowCnt = 1
        # for (int i = 1; i < points.length; i++)
        for i in range(1,len(points)):
            if (arrowPos >= points[i][0]): continue
            arrowCnt+=1
            arrowPos = points[i][1]
        
        return arrowCnt
    