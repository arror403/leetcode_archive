class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        
        # For each starting row
        for up in range(m):
            h = [1] * n  # Heights of consecutive 1s ending at current row
            
            # Extend downward from starting row
            for down in range(up, m):
                # Update heights: if current cell is 0, height becomes 0
                for k in range(n):
                    h[k] = h[k] if mat[down][k] else 0
                
                # Count submatrices in current row using histogram technique
                res += self.countSubarrays(h)
        
        return res
    
    def countSubarrays(self, heights):
        """Optimized: Count subarrays with all positive values in O(n)"""
        total = length = 0
        for h in heights:
            length = length + 1 if h > 0 else 0
            total += length
        return total