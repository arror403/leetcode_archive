class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n=len(points),len(points[0])
        dp=points[0]
        
        for i in range(1, m):
            new_dp=[0]*n
            left_max=[0]*n
            right_max=[0]*n
            
            # Calculate left_max
            left_max[0]=dp[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j-1]-1, dp[j])
            
            # Calculate right_max
            right_max[-1]=dp[-1]
            for j in range(n-2, -1, -1):
                right_max[j] = max(right_max[j+1]-1, dp[j])
            
            # Update new_dp
            for j in range(n):
                new_dp[j] = points[i][j]+max(left_max[j], right_max[j])
            
            dp = new_dp
        

        return max(dp)