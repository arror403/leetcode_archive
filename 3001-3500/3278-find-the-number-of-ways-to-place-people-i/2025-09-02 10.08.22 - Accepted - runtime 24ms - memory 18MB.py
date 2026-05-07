class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res=0
        L=len(points)

        points.sort(key=lambda x:(x[0], -x[1]))

        for i in range(L):
            max_y=-inf
            for j in range(i+1, L):
                if points[i][0]<=points[j][0] and points[i][1]>=points[j][1]:
                    if points[j][1] > max_y:
                        res+=1
                        max_y=points[j][1]

                    # max_y = max(max_y, points[j][1])


        return res