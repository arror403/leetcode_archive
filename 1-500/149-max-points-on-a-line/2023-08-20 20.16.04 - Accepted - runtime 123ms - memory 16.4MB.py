class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        max_points = 2  # At least 2 points are needed to form a line

        for i, p1 in enumerate(points):
            slope_count = defaultdict(int)
            duplicates = 0
            verticals = 0

            for j, p2 in enumerate(points):
                if i != j:
                    dx = p2[0] - p1[0]
                    dy = p2[1] - p1[1]

                    if dx == 0:
                        if dy == 0:
                            duplicates += 1
                        else:
                            verticals += 1
                    else:
                        tmp=math.gcd(dy,dx)
                        dx,dy=dx/tmp,dy/tmp
     
                        slope = (dy, dx)
                        slope_count[slope] += 1

            max_points = max(max_points, duplicates + 1 + max(verticals, max(slope_count.values(), default=0)))

        return max_points