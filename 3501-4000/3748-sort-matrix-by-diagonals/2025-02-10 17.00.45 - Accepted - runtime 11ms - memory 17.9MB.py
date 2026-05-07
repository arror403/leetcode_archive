class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)  # Matrix is n x n
        # Dictionary to store diagonals
        diags = {}
        
        # Collect elements in each diagonal
        for i in range(n):
            for j in range(n):
                diag_idx = i - j  # Use difference as diagonal index
                if diag_idx not in diags:
                    diags[diag_idx] = []
                diags[diag_idx].append(grid[i][j])
        
        # Sort diagonals based on their position
        for k in diags:
            if k >= 0:  # Bottom-left triangle (including main diagonal)
                diags[k].sort(reverse=True)  # Non-increasing order
            else:  # Top-right triangle
                diags[k].sort()  # Non-decreasing order
        
        # Reconstruct the matrix
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diag_idx = i - j
                result[i][j] = diags[diag_idx].pop(0)
        
        return result