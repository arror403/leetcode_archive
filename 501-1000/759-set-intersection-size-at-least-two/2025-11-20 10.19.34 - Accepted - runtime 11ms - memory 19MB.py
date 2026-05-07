class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 1. Sort intervals. 
        # Primary key: End point (ascending). We want to process intervals that finish earliest.
        # Secondary key: Start point (descending). If ends are same, process the shorter one first (requires fewer points).
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # 'points' acts like your 'used' set, but we keep it sorted list to check overlaps easily
        points = [] 
        
        for a, b in intervals:
            # Check how many points we already have that fall into current interval [a, b]
            # Since 'points' is sorted and we process by end time, we only need to check the last 2 added points.
            
            overlap_count = 0
            if points and points[-1] >= a:
                overlap_count += 1
            if len(points) >= 2 and points[-2] >= a:
                overlap_count += 1
                
            # We need total 2 points. 
            # Strategy: Always pick the largest possible numbers (rightmost) to maximize overlap with future intervals.
            
            if overlap_count == 0:
                # We have 0 points, need 2. Pick 'b-1' and 'b'.
                points.append(b - 1)
                points.append(b)
                
            elif overlap_count == 1:
                # We have 1 point (it must be the largest one we added previously), need 1 more.
                # Note: The existing point might be 'b'. If so, we'd need 'b-1'. 
                # But because we sort by end time, the existing point from a previous interval 
                # is usually <= b. We pick 'b' to extend reach to the right.
                points.append(b)
                
            # If overlap_count == 2, we are already good. Do nothing.

        return len(points)